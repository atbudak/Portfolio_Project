#!/bin/bash

$number=1

while [[ $number -le 10 ]]
do
	echo $number
	((number++))
done
echo "number is $number"

