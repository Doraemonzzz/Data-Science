# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:44:02 2018

@author: Administrator
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    n=len(L)
    if(n==0):
        return float('NaN')
    else:
        s=0
        length=[]
        for i in L:
            l=len(i)
            length.append(l)
            s+=l
        avg=s/n
        var=0
        for i in length:
            var+=(i-avg)**2
        return (var/n)**0.5
    
L = ['a', 'z', 'p']
print(stdDevOfLengths(L))
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))


def cov(L):
    n=len(L)
    s=0
    for i in L:
        s+=i
    avg=s/n
    var=0
    for i in L:
        var+=(i-avg)**2
    var=(var/n)**0.5
    return var/avg
L=[10, 4, 12, 15, 20, 5]
print(cov(L))

        