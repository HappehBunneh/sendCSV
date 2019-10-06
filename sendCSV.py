#!/usr/bin/python

import smtplib
import json
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from zipfile import ZipFile
import time

with open("config.json", "r") as file:
	data = json.load(file)
print(data)

dir=data["directory"]
filenames = [os.path.join(dir, i) for i in os.listdir(dir) if i[-3:] == "csv"]
filename = time.strftime("%Y-%m-%d.zip")

with ZipFile(filename, "w") as zip:
	for file in filenames:
		zip.write(file)

username=data["username"]
password=data["password"]

message = MIMEMultipart()
message["From"] = data["username"]
message["To"] = data["sendTo"]
message["Subject"] = "CSV from sendCSV"
body = "Sent from sendCSV"
message.attach(MIMEText(body, "plain"))
with open(filename, "rb") as attachment:
	part = MIMEBase("application", "octet-stream")
	part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment; filename={0}".format(filename))
message.attach(part)
text = message.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(username, data["sendTo"], text)
server.quit()
