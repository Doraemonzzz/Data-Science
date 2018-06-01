# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:18:48 2018

@author: Administrator
"""

with open('companies.txt') as f1:
    company=f1.readlines()
    
for i in range(len(company)):
    company[i]=str(i+1)+' '+company[i]
    
with open('scompanies.txt','w') as f2:
    f2.writelines(company)