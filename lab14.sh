#!/bin/bash
# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 

whoami
ifconfig

echo "Common IP addresses are as follows."
echo "142.250.217.78 for google.com."
echo "142.251.33.69 for gmail.com."
echo "157.240.3.35 for facebook.com."

echo "Enter an IP address to check connectivity."
read IP
COUNT=1

if ping -c $COUNT $IP > /dev/null 2>&1; then
    echo "Ping to $IP was successful."
else
    echo "Ping to $IP failed."
fi