#!/bin/bash
touch /tmp/start2.txt
while [ ! -d "/media/yourusernamehere/HOLGA/DCIM/100MEDIA" ]; do
    sleep 10
done
python /opt/holga.py
if (($? > 0)); then
    touch /tmp/fail.txt
    exit 1
fi
touch /tmp/greatSuccess.txt

