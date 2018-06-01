# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:56:47 2018

@author: Administrator
"""

import re

a=['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
Name=[]
Price=[]

for i in a:
    name=""
    price=""
    for j in i:
        if j.isalpha():
            name+=j
        elif j.isalnum():
            price+=j
    Name.append(name)
    Price.append(price)

print("{0:<10s}\t{1:10s}\t{2:10s}".format("num","name","price"))    
for i,j,k in zip(range(1,len(Name)+1),Name,Price):
    print("{0:<10d}\t{1:10s}\t{2:10s}".format(i,j,k))