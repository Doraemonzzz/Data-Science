# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:33:37 2018

@author: Administrator
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    start=0
    while(1):
        if(test(start)==True):
            return start
        elif (test(-start)==True):
            return -start
        start+=1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))