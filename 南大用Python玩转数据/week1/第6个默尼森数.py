# -*- coding: utf-8 -*-
"""
Created on Thu May 24 22:29:05 2018

@author: Administrator
"""

from math import sqrt
from math import log

def prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        m=int(sqrt(num))+1
        for i in range(2,m):
            if num%i==0:
                return False
        return True
    
def monisen(no):
    count=0
    n=3
    while(count<=no):
        m=log(n+1,2)
        if(m==int(m) and prime(n)):
            if(prime(m)):
                count+=1
                print(n)
        n+=1
monisen(6)
