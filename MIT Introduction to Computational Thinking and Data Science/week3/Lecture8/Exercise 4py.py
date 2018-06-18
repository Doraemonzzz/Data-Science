# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 22:16:04 2018

@author: Administrator
"""

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    import random
    cnt=0
    for i in range(numTrials):
        ball=[1,1,1,0,0,0]
        ans=[]
        for j in range(3):
            temp=random.choice(ball)
            ball.remove(temp)
            ans.append(temp)
        if ans==[0,0,0] or ans==[1,1,1]:
            cnt+=1
    return cnt/numTrials

n=noReplacementSimulation(100000)
print(n)
    