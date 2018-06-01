# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:50:01 2018

@author: Administrator
"""

text=[]
with open('Blowing in the wind.txt') as file:
    for i in file.readlines():
        text.append(i)
        
text.insert(0,"Blowin' in the wind\n")
text.insert(1,"Bob Dylan\n")
text.append("1962 by Warner Bros. Inc.")

with open('Blowing in the wind.txt','w') as file:
    file.writelines(text)
    
for i in text:
    print(i)