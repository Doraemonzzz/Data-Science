# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:02:30 2018

@author: Administrator
"""

def max_contig_sum(L):
    n=len(L)
    sum1=sum2=0
    for i in range(n):
        sum1+=L[i]
        if(sum1>sum2):
            sum2=sum1
        elif(sum1<0):
            sum1=0
    return sum2

a=[3, 4, -1, 5, -4]
print(max_contig_sum(a))
b=[3, 4, -8, 15, -1, 2]
print(max_contig_sum(b))