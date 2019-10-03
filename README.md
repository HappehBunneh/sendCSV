# sendCSV
Shell script to send the latest csv file made

Prerequisites:

* Mutt (`sudo apt-get install mutt`)
* Sendmail (`sudo apt-get install sendmail`)

To run:
	
`./sendCSV.sh`

Edit variables within `sendCSV.sh`:

* `DIRPATH`
* `SUBJECT`
* `RECIPIENT`

If not set as executable:
	
`sudo chmod 775 sendCSV.sh`
