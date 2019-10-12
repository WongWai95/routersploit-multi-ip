#!/bin/bash

echo "routersploit running!"
echo "--------------------------"

for ip in $(cat ip_range.txt)
do
    echo 'scanning ip: '$ip
    sudo python3 rsf-scanner.py $ip > scanner_output/$ip.rsr
done

echo "--------------------------"
echo "done!"
