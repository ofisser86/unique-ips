#!/usr/bin/bash

# get the last <$2> lines
tail -$2 $1 > tmp.txt

grep -oE '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' tmp.txt | sort | uniq
# sort and search all uniq ip adresess
# uniq_ips=$(awk '{ print $2 }' tmp.txt | sort | uniq)
rm tmp.txt