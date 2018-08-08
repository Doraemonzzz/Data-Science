# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:39:52 2018

@author: Administrator
"""

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    n=0.0
    for i in range(numTrials):
        ball=[1]*4+[0]*4
        score=0
        for j in range(3):
            temp=random.choice(ball)
            ball.remove(temp)
            score+=temp
        if (score==3):
            n+=1
    return 2*n/numTrials

print(drawing_without_replacement_sim(10000))