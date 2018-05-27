# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:55:03 2018

@author: Administrator
"""
from math import sqrt

def isPrime(x):
    if x==1:
        return False
    elif x==2:
        return True
    else:
        m=int(sqrt(x))+1
        for i in range(2,m):
            if x%i==0:
                return False
        return True

count=0
s=""

for i in range(4,2001,2):
    if(count%6==0 and count>0):
        print(s)
        s=""
    for j in range(2,i):
        if isPrime(j) and isPrime(i-j):
            s+=str(i)+"="+str(j)+"+"+str(i-j)+" "
            break
    count+=1
