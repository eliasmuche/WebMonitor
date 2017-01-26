#! /usr/bin/gnuplot
#Elias Muche 
#11/25/16
#HW4:Part 3

set terminal png 
set output 'output.png'
set title 'One Minute Rate Over Time'
set xlabel 'Time(10s seconds)'
set ylabel 'One Minute Rate'

plot 'alteredData.tsv' using 1:2 with lines title '200s', 'alteredData.tsv' using 1:3 with lines title '400s', 'alteredData.tsv' using 1:4 with lines title '500s'