# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:45:39 2013

@author: g_singhal
"""

from collections import Counter
from collections import deque
import sys
sys.setrecursionlimit(1000000)
import resource
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
      
def DFS(Graph,start_node):
    global time
    global explored
    global finOrder
    global leader
    
    explored |= {start_node}
    #leader[start_node-1] = source_node
        
    for leaf_node in Graph[start_node]:
        if leaf_node not in explored: 
            DFS(Graph,leaf_node)
    
    finOrder.append(start_node)    
    leader.append(source_node)    
    
    time = time+1
    #finishTime[start_node-1] = time
    print 'time='+str(time)
    if time==19608:
        print 'source_node=' +str(source_node)
        print 'start_node=' +str(start_node)

def DFSLoop(Graph):
    global source_node
                
    for node in G:
        source_node = N+1-node
        if source_node not in explored:
            print 'source_node=' +str(source_node)
            DFS(Graph,source_node)
    
N = 875714
G = range(1,N+1)
Graph = dict((node,[]) for node in G)
RevGraph = dict((node,[]) for node in G)

with open('/Users/g_singhal/Desktop/SCC.txt') as f:
  for line in f:
    data = [int(x) for x in line.split()]
    Graph[data[0]].append(data[1])
    RevGraph[data[1]].append(data[0])

print 'Data Input Done!'

time = 0
source_node = 0
explored = set()
finOrder = deque()
#finishTime = [0]*N
leader = deque()

DFSLoop(RevGraph)
del RevGraph

print 'First Loop Done!'

TimeGraph = {}
finTimeDict = dict(zip(finOrder,G))
for node in G:
    TimeGraph[finTimeDict[node]] = [finTimeDict[i] for i in Graph[node]]
del Graph
del finTimeDict

print 'Second Graph Created!'
 
time = 0   
source_node = 0
explored = set()
finOrder = deque()
leader = deque()

DFSLoop(TimeGraph)

print 'Second Loop Done!'

print Counter(leader).most_common(5)