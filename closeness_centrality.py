# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:45:29 2013
@author: g_singhal
"""

import Queue
import pdb

#Create function for Breadth First Searh
def BFS(Graph, start, end):
    q = Queue.Queue()
    path = [start]
    q.put(path)
    visited = set([start])
    while not q.empty():
        path = q.get()
        last_node = path[-1]
        if last_node == end:
            return path
        for node in Graph[last_node]:
            if node not in visited:
                visited.add(node)
                q.put(path + [node])

#Read in Data File
Graph = {}
with open('/Users/g_singhal/Desktop/internet.txt') as f:
  for line in f:
    data = [int(x) for x in line.split()]
    Graph[data[0]] = sorted(data[1:])

#Initialize variables
N = 22963
vrtxList = range(0,N)
shortestPaths = [0]*N
vrtx_i = 0    

#Use Breadth-first Search to find Shortest Paths
for vrtx_j in vrtxList:
    if vrtx_i!=vrtx_j:
        shortestPaths[vrtx_j] = len(BFS(Graph,vrtx_i,vrtx_j))-1
    
#Average Shortest Paths to find Centrality
vrtxCentrality = float(sum(shortestPaths))/float((N-1))

print "Closeness Centrality for Node Zero is"
print vrtxCentrality
pdb.set_trace() 

