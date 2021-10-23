#!/bin/bash

echo "Input is : "

for var in $(ls -l | cut -d' ' -f8-9)
do
	echo $var
done

