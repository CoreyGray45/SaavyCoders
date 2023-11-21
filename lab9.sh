#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry
echo "1. Hello World"
echo "2. Ping a website or IP address"
echo "3. Run ifconfig"
read "enter 1-3"
user=y

while [ $user=y ]
do
read input 
    if [ $input=1 ]
    then echo "Hello World"
    elif [ $input=2 ]
        then 
            echo "Enter website or ip address to ping:"
            read address
            ping -c 5 $address 
    elif [ $input=3 ]
        then 
            ifconfig
            echo "Invalid entry"
    fi
    echo "Do you want to play again: Y/N"
    read user 
done   
    echo "Good Work"