# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:58:02 2013

@author: g_singhal
"""

#import csv
#file = open('/Users/g_singhal/Desktop/KargerMinCut.txt', 'rb')
#data = csv.reader(file, delimiter='\t')
#table = [row for row in data]
#
#for i in range(len(table)):
#    table[i].remove('')
#    table[i].pop(0)
#
#Nodes = range(1,201)
#Node2Vert = dict(zip(Nodes, table))
#

from collections import Counter
import random

def MinCut(Node2Vert):
    
    while len(Node2Vert)>2:
        
        #choose first vertex at random        
        v1 = random.choice(Node2Vert.keys())
        vertCount1 = Node2Vert[v1]
        
        #choose second vertex to be the one with max edges
        v2 = vertCount1.most_common(1)[0][0]
        vertCount2 = Node2Vert[v2]
        vertices2 = vertCount2.keys()
        
        #merge vertices adjacency lists
        vertCount1.update(vertCount2)
        
        #delete self-loops
        del vertCount1[v1]
        del vertCount1[v2]
        
        #remove v2 from graph
        del Node2Vert[v2]
        Node2Vert[v1] = vertCount1
        
        #replace all references to v2 w/ v1
        for vertex in vertices2:
            if vertex!=v1:
                cnt = Node2Vert[vertex].pop(v2)
                Node2Vert[vertex].update({v1 : cnt})

    return Node2Vert

Node2Vert = {}
with open('/Users/g_singhal/Desktop/KargerMinCut.txt') as f:
  for line in f:
    data = [int(x) for x in line.split()]
    Node2Vert[data[0]] = Counter(data[1:])

num_cuts = []
for i in range(1000):
    X = MinCut(Node2Vert)
    num_cuts.append(X.values()[0].values()[0])

print min(num_cuts)


        
        
        
        
        
        
        
