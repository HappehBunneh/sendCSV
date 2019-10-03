#!/bin/sh

DIRPATH="dirPath"
SUBJECT="CSV Delivery"
RECIPIENT="email"

cd $DIRPATH
CSVFILE=$(ls -t *.csv | head -1)
echo $CSVFILE
echo "Sent via sendCSV" | mutt -a $CSVFILE -s $SUBJECT -- $RECIPIENT
