# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:36:34 2013

@author: g_singhal
"""
import pdb

graph = {}
with open('/Users/g_singhal/Desktop/dijkstraData.txt','rb') as f:
    for line in f:
        data = line.split()
        parent_node = int(data[0])

        data = data[1:]        
        child_node = []
        distance = []
        
        for node in data:
            couplet = node.split(',')
            child_node.append(int(couplet[0]))
            distance.append(int(couplet[1]))
        
        graph[parent_node] = dict(zip(child_node, distance))

def Dijkstra(graph,start,end):
    import heapq
    
    explored = set()
    distances = {}
    path = {}
    queue = []
    
    heapq.heappush(queue,[0,'',start])
    stop = 0    
    
    while len(queue)>0 and stop==0:
        distance, parent, node = heapq.heappop(queue)
        
        if node not in explored:

            #print 'node explored is '+str(node)
            
            explored |= {node}
            distances[node] = distance
            path[node] = parent
            
            if node==end:
                stop=1
                return distance, path
            else:
                for successor,length in graph[node].iteritems():
                    if successor not in explored:
                        new_dist  = distance+length
                        new_entry = [new_dist,node,successor]
                        
                        if successor not in distances:
                            
                            distances[successor] = new_dist
                            path[successor] = node
                            heapq.heappush(queue,new_entry)

                        elif new_dist < distances[successor]:
                    
                            q_index = queue.index([distances[successor],path[successor],successor])
                            distances[successor] = new_dist
                            path[successor] = node
                            queue[q_index] = new_entry
                            heapq.heapify(queue)

dist = Dijkstra(graph,1,7)
print 'distance to 7 is '+str(dist[0])

dist = Dijkstra(graph,1,37)
print 'distance to 37 is '+str(dist[0])

dist = Dijkstra(graph,1,59)
print 'distance to 59 is '+str(dist[0])

dist = Dijkstra(graph,1,82)
print 'distance to 82 is '+str(dist[0])

dist = Dijkstra(graph,1,99)
print 'distance to 99 is '+str(dist[0])

dist = Dijkstra(graph,1,115)
print 'distance to 115 is '+str(dist[0])

dist = Dijkstra(graph,1,133)
print 'distance to 133 is '+str(dist[0])

dist = Dijkstra(graph,1,165)
print 'distance to 165 is '+str(dist[0])

dist = Dijkstra(graph,1,188)
print 'distance to 188 is '+str(dist[0])

dist = Dijkstra(graph,1,197)
print 'distance to 197 is '+str(dist[0])