# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:41:57 2018

@author: Administrator
"""

try:
    score=int(input("请输入分数:"))
    if(score>=0 and score<=59):
        print("D")
    elif(score<=69):
        print("C")
    elif(score<=89):
        print("B")
    elif(score<=100):
        print("A")
    else:
        print("Invalid score")
except:
    print("Invalid score")