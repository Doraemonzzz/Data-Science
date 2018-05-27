# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:29:02 2018

@author: Administrator
"""

while(True):
    count=input("Enter count: ")
    price=input("Enter price for each one: ")
    try:
        count=int(count)
        price=float(price)
        print("The price is {}".format(count*price))
        break
    except:
        print("Error, please enter numeric one.")
