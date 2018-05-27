# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:17:12 2018

@author: Administrator
"""
from math import sqrt
m=int(input())

ans=str(m)+"="

def isPrime(x):
    if x==2:
        return True
    else:
        m=int(sqrt(x))+1
        for i in range(2,m):
            if x%i==0:
                return False
        return True
    
while(not isPrime(m)):
    for i in range(2,m):
        if isPrime(i) and m%i==0:
            ans+=str(i)+"*"
            m=int(m/i)
            break
ans+=str(m)

print(ans)

