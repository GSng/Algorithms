# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:46:16 2013

@author: g_singhal
"""

import numpy

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    
    print middle
    print lst
    print left
    print right
    
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count, i, j = 0, 0, 0
   
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left[i:])
            j += 1
            
#        print i
#        print j
#        print count
#        print result
        
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

A = [5,3,8,9,1,7,0,2,6,4]#numpy.loadtxt('/Users/g_singhal/Desktop/IntegerArray.txt')
print count_inversion(A)
