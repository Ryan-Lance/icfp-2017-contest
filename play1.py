#!/usr/bin/env python2
import json
import csv
import numpy as np
from random import randint
from rw import readMessage, writeMessage

with open('examples/setup.sample') as f:
    handshake = readMessage(f)
    setup = readMessage(f)


sites = setup['map']['sites']
rivers = setup['map']['rivers']
mines = setup['map']['mines']


for i in range(len(sites)):
	sites[i]['neighbors'] = []

for i in range(len(rivers)):
	rivers[i]['taken'] = False
	rivers[i]['ours'] = False
	s = rivers[i]['source']
	t = rivers[i]['target']
	print "s = ", s, "t = ", t
	if (s != None and t != None):
		sites[t]['neighbors'].append(s)
		sites[s]['neighbors'].append(t)


# print all neighbors
for i in range(len(sites)):
	print "Site: ", sites[i]['id'],",has neighbors: ", sites[i]['neighbors']


# play
def omove():
	chosen = findFreeMoves()
	if chosen == None: return
	rivers[chosen]['taken'] = True
	rivers[chosen]['ours' ] = False
	
def pmove():
	chosen = findFreeMoves()
	if chosen == None: return
	rivers[chosen]['taken'] = True
	rivers[chosen]['ours' ] = True

def findFreeMoves():
	free = []
	for i in range(len(rivers)):
		if rivers[i]['taken'] == False:
			free.append(i)
	print "Free = ", free
	if len(free) == 0:
		return None
	c = randint(0, len(free)-1)
	chosen = free[c]
	print "Chosen = ", chosen
	return chosen

for i in range(len(rivers)):
	print "River #:", i, ", Taken?: ", rivers[i]['taken'], ", Ours?: ",rivers[i]['ours']

print "\nLet  there be moves..."
for i in range(len(rivers)/2):
	omove()
	pmove()


for i in range(len(rivers)):
	print "River #:", i, ", Taken?: ", rivers[i]['taken'], ", Ours?: ",rivers[i]['ours']
