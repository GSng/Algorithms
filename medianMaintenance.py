# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:22:21 2013

@author: g_singhal
"""

import heapq
import pdb

def medianMaintain(x):
     global lst
     
     lst = lst.append(x)
     pdb.set_trace()
     lst = sorted(lst)
     N = len(lst)
     
     if N%2==0:
         k = N/2
     else:
         k = (N+1)/2
         
     return lst(k-1)
    
#    global heap_hi # minheap
#    global heap_lo # all entries multiplied by -1  (max heap)  
#    
#    #insert new element
#    if len(heap_lo)==0:
#        heapq.heappush(heap_lo,-x)
#    else:
#        #pdb.set_trace()
#        if x>-heap_lo[0]:
#            heapq.heappush(heap_hi,x)
#            
#            if len(heap_hi)>len(heap_lo):
#                heapq.heappush(heap_lo,-(heapq.heappop(heap_hi)))
#            
#        else:
#            heapq.heappush(heap_lo,-x)
#            
#            if len(heap_lo)>(len(heap_hi)+1):
#                heapq.heappush(heap_hi,-(heapq.heappop(heap_lo)))
#        
#    return -heap_lo[0]
    
lines = open('/Users/g_singhal/Desktop/median.txt').read().splitlines()
A = map(lambda x: int(x), lines)      
del lines

heap_hi = []
heap_lo = []

lst = [-1]

medians = [medianMaintain(a) for a in A]
print (sum(medians)%1000)
    
