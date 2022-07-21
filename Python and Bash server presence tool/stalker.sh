#!/bin/bash

file_name=$(date "+%Y-%m-%d")

last -n 0 -w --time-format iso --since yesterday >"placeholder1"

head -n -2 "placeholder1" >"placeholder2"
rm "placeholder1"

sed "s/ - /-/g" "placeholder2" >"placeholder1"
rm "placeholder2"

sed "s/ /,/g" "placeholder1" >$HOME/projects/bash-stalker/stalker_logs/"$file_name.txt"
rm "placeholder1"