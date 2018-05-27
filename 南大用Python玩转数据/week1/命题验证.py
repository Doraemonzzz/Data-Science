# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:46:16 2018

@author: Administrator
"""

flag=1
for i in range(100,1000):
    if i%37:
        n1=10*(i%100)+i//100
        n2=100*(i%10)+i//10
        if(n1%37 and n2%37):
            pass
        else:
            flag=0
            break
print(flag)