#!/bin/bash

echo "Numbers: "

for number in 0 1 2 3 4 5 6 7 8 9
do
	 echo $number
done

echo "Names:"

for name in Joe David Matt John Timothy
do
	   echo $name
done

for file in `pwd`/*
do
	   echo $file
done


