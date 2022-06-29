#!/bin/sh
printf "Hi, Press 1 to fetch whole JSON or 2 to fetch perticular key\n"
read input1
if [ $input1 -eq 1 ]
then
        metadata_JSON=$(python3 getjson.py)
        echo "output is"
        printf '%s\n' "$metadata_JSON"
elif [ $input1 -eq 2 ]
then
        python3 getkeyvalue.py
else
        printf "Invalid input\n"
        exec $0
fi