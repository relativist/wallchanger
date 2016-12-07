#!/bin/bash

dir=/home/sit/wall
time=120



array=($(ls $dir))
count=${#array[@]}
let count=count-1 
echo "count="$count
next=$((1 + RANDOM % $count))

COUNTER=0
while [  $COUNTER -lt 900 ]; do
        next=$((1 + RANDOM % $count))
        second=$((1 + RANDOM % $count))
	firstImage=$dir/${array[$next]}
	secondImage=$dir/${array[$second]}
	echo $firstImage $secondImage
        feh --bg-fill $firstImage $secondImage
        sleep $time
        let COUNTER=COUNTER+1 
done
