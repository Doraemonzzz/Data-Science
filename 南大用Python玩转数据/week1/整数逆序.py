# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:14:05 2018

@author: Administrator
"""

#整数逆序
n=int(input())

m=""
while(n>0):
    m+=str(n%10)
    n//=10

print(m)
    