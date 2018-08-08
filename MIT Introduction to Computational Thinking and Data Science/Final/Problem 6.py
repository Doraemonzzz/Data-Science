# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:33:43 2018

@author: Administrator
"""

import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    
    def gen(n):
        if n==1:
            return [[0],[1]]
        else:
            temp=gen(n-1)
            result=[]
            for i in temp:
                result.append([0]+i)
                result.append([1]+i)
            return result

    choices=np.array(choices)
    b=np.array(gen(len(choices)))
    eq=[]
    le=[]
    for bins in b:
        r=bins*choices
        if (r.sum()==total):
            eq.append(bins)
        elif (r.sum()<total):
            le.append(bins)
    if (len(eq)>0):
        result=min(eq,key=lambda x:sum(x))
    else:
        result=max(le,key=lambda x:sum(x*choices))
    return np.array(result)

#choices=[1,2,2,3]
#total=4
#print(find_combination(choices,total))
#choices = [1,1,3,5,3]
#total = 5
#print(find_combination(choices,total))
#choices = [1,1,1,9]
#total = 4
#print(find_combination(choices,total))
#print(gen(3))
#choices=[5,4]
#total=2
#print(find_combination(choices,total))
    
print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171))
                