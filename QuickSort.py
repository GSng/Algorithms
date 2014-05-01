# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:20:36 2013

@author: g_singhal
"""

import numpy

compTotal = 0
#        B =  [L,k,R-1]   
#        C = [A[i] for i in B]
#        p = int(numpy.median(C))
#        ind = numpy.where(A==p)
        
def Partition(A,L,R,pivType):
    
    if pivType=='R':
        A[L],A[R-1] = A[R-1],A[L]
    elif pivType=='M':
        if (L+R)%2==0:
            k = (L+R)/2
        else:
            k = (L+R+1)/2 
            
        if A[k]<A[L] and A[L]<A[R-1]:
            p_idx = L
        elif A[k]<A[R-1] and A[R-1]<A[L]:
            p_idx = R-1
        elif A[L]<A[k] and A[k]<A[R-1]:
            p_idx = k
        elif A[R-1]<A[k] and A[k]<A[L]:
            p_idx = k
        elif A[R-1]<A[L] and A[L]<A[k]:
            p_idx = L
        elif A[L]<A[R-1] and A[R-1]<A[k]:
            p_idx = R-1
            
        A[L],A[p_idx] = A[p_idx],A[L]

    p = A[L]      
    i = L+1
    for j in range(L+1,R):
        if A[j] < p:
            A[i],A[j] = A[j],A[i]
            i=i+1
    A[L],A[i-1] = A[i-1],A[L]
    return i-1


def QuickSortHelper(A,L,R):
    if L<R:
        global compTotal
        compTotal+=R-L-1
        
        splitIndex = Partition(A,L,R,'M')
        QuickSortHelper(A,L,splitIndex)
        QuickSortHelper(A,splitIndex+1,R)

def QuickSort(A):
    QuickSortHelper(A,0,len(A))
    return A
    
def isSorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False
    return True

A = numpy.loadtxt('/Users/g_singhal/Desktop/QuickSort.txt')
A = QuickSort(A)
print isSorted(A)
print compTotal