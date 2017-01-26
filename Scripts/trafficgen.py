#! /usr/bin/python2.7

import sys
import time
import sched as sc
import urllib2 as u
import random as ran 
import argparse as ar

#Elias Muche 
#11/16/16
#HW4:Part 1

parse=ar.ArgumentParser()

parse.add_argument('--url',help='--url <your url>',required=True)
parse.add_argument('--rps',help='--rps <your rps>',required=True)
parse.add_argument('--jitter',help='--jitter <your jitter>',required=True)
parse.add_argument('--dur',help='--dur <your duration>',required=True)

args=parse.parse_args()
url=args.url
rps=int(args.rps)
jitter=float(args.jitter)
dur=int(args.dur)

begin=int((rps)*(1-jitter))
end=int((rps)*(1+jitter))
rate=ran.randint(begin,end)

def genTraffic():
	start=time.time()
	s=sc.scheduler(time.time,time.sleep)
	while time.time()-start <= dur :
		s.enter(1,1,populate,())
		s.run()
				
def populate():
	for i in xrange(0,int(rate)):
		try:
			u.urlopen(url)
		except:
			pass

genTraffic()