#! /bin/bash

#Elias Muche 
#11/22/16
#HW4:Part 1 & 2


python trafficgen.py --url http://localhost:8080 --rps 541 --jitter .55 --dur 3600 &
python trafficgen.py --url http://localhost:8080/blah --rps 232 --jitter .32 --dur 3600 &
python trafficgen.py --url http://localhost:8080/fail --rps 100 --jitter .55 --dur 3600 &
python collector.py --url http://localhost:8080/stats --interval 10 --dur 3600 >data.tsv &