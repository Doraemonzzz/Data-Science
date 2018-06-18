# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:11:39 2018

@author: Administrator
"""

#比较numpy速度
import time
import math
import numpy as np
x=np.arange(0,100,0.01)
t_m1=time.clock()
for i,t in enumerate(x):
    x[i]=math.pow((math.sin(t)),2)
t_m2=time.clock()
y=np.arange(0,100,0.01)
t_n1=time.clock()
y=np.power(np.sin(y),2)
t_n2=time.clock()
print('Running time of math:', t_m2 - t_m1)
print('Running time of numpy:', t_n2 - t_n1)