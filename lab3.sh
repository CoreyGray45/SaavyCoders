#!/bin/bash
echo "enter a number"
sleep 1
read number
variable=number

echo "Your number is $number"

if(($number>5))
then echo "number is greater than five"
elif(($number<5))
then echo "Your number is less than five"
else echo "Your number is five"
fi
