#! /bin/usr/python2.7


#Elias Muche 
#11/18/16 
#HW4:Part 3

import sys
import math

data=sys.argv[1]
times=[]
fives=[]
twos=[]
fours=[]

f=open(data)
for line in f:
  line=line.rstrip('\n')
  if len(line) > 1:
    times.append(int(line.split('\t')[0]))
    fives.append(int(line.split('\t')[1]))
    twos.append(int(line.split('\t')[2]))
    fours.append(int(line.split('\t')[3]))

minute=1
graphData=""
for i in range(len(times)-6):
	graphData+=str(i)+"\t"
	diffFive=abs((fives[i]-fives[i+6])/60)
	diffFour=abs((fours[i]-fours[i+6])/60)
	diffTwo=abs((twos[i]-twos[i+6])/60)
	#print i,"\n"
	#print i-6
	#print "\n\n"
	graphData+=str(diffTwo)+"\t"+str(diffFour)+"\t"+str(diffFive)+"\n"

	minute+=1

print graphData