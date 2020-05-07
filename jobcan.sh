#!/bin/bash

echo "Choose your action from start, end, start-rest, end-rest"
read input
python3 `dirname $0`/jobcan_selenium.py $input
