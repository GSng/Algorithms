from math import log
import numpy
from numpy import empty 
import Queue
import pdb

#Create function for Breadth First Searh
def BFS(Graph, start):
    q = Queue.Queue()
    q.put(start)
    visited = set([start])
    while not q.empty():
        last_node = q.get()
        for node in Graph[last_node]:
            if node not in visited:
                visited.add(node)
                q.put(node)    
    
    return visited

def config_graph(n,p1):
    graph = {i: [] for i in range(1,n+1)}
    edges = {}
    
    #create graph
    m = 3
    while m%2==1:
        for i in range(1,n+1):
            trial = numpy.random.binomial(1,p1)
            if trial==0:
                edges[i] = 1
            else:
                edges[i] = 3
        m = sum(edges.values())/2
    
    nodes = range(1,n+1)        
    for i in range(1,n+1):
        if len(graph[i]) < edges[i]:
            nodes.remove(i)
            for j in range(edges[i]-len(graph[i])):
                k = nodes[numpy.random.randint(0,len(nodes))]
                while (k in graph[i]) | (i in graph[k]) | (len(graph[k])>=edges[k]):
                    if (len(graph[k])>=edges[k]):
                        nodes.remove(k)
                    if len(nodes)==0:
                        return graph
                    k = nodes[numpy.random.randint(0,len(nodes))]
                     
                graph[i].append(k)
                graph[k].append(i)
        else:
            if i in nodes:
                nodes.remove(i)
    
    return graph

def largest_component(graph):
    component_size = 0
    nodes = graph.keys()

    while len(nodes)>0:
        s = BFS(graph,nodes[1])
        for i in s:
            nodes.remove(i)
        cs = len(s)
        if component_size<cs:
            component_size = cs
    
    return component_size

x = []    
for p in range(11,101):
   x.append(largest_component(config_graph(10000,p*0.01)))
   print p
   print x[-1]
print x
import matplotlib
pdb.set_trace()