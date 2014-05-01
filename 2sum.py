# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:24:35 2013

@author: g_singhal
"""
import math
  
lines = open('/Users/g_singhal/Desktop/algo1-programming_prob-2sum.txt').read().splitlines()
A = map(lambda x: int(x), lines)      
A = sorted(A)
del lines

N = len(A)
amin = min(A)
amax = max(A)

numBins = int(math.ceil((amax-amin)/20001.0))
hashdict = dict((Bin,[]) for Bin in range(1,numBins+1))
for a in A:
    Bin = max(int(math.ceil((a-amin)/20001.0)),1)
    hashdict[Bin].append(a)

targetdict = dict((x,0) for x in range(-10000,10001))

for a in A:
    ub = 10000-a
    lb = -10000-a

    ubBin = min(max(int(math.ceil((ub-amin)/20001.0)),1),numBins)
    lbBin = max(min(int(math.ceil((lb-amin)/20001.0)),numBins),1)    
    
    if ubBin==lbBin:
        interval = hashdict[ubBin]
    else:
        interval = hashdict[lbBin]+hashdict[ubBin]
    
    if len(interval)>0:
        Y = [y for y in interval if y<=ub and y>=lb]
        
        if len(Y)>0:
            targets = [a+y for y in Y]
            for t in targets:
                if t!=a:
                    targetdict[t] = 1

count = sum(targetdict.values())        
print count

#for key in targetdict.keys():
#    if targetdict[key]:
#        print key
