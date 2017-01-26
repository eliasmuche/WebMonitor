#! /bin/usr/python2.7


#Elias Muche 
#11/16/16
#HW4:Part 2

import sys 
import requests
import time
import urllib2 as u
import argparse as ar

parse=ar.ArgumentParser()
parse.add_argument('--url',help='format is --url <yourURL>',required=True)
parse.add_argument('--interval',help='format is --interval <your interval(seconds)>',required=True)
parse.add_argument('--dur',help='format is --dur <your duration(seconds)>',required=True)
args=parse.parse_args()

url=args.url
interval=int(args.interval)
dur=int(args.dur)
string=""

def collectStats(URL):
	string=""
	startTime=time.time()
	while time.time()-startTime <= dur:#change 21 to 3601
		if ((time.time()-startTime) % interval) == 0:
			site=u.urlopen(URL)
			site=site.read()
			site=site.split('\n')
			site=site[:len(site)-1]
			for piece in site:
				string=string+piece.split(' ')[1] +"\t" 
			string=string+'\n'	
	print string			
		
collectStats(url)


