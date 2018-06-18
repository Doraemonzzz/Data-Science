# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 21:01:29 2018

@author: Administrator
"""

import numpy as np
from sklearn.cluster import KMeans
list1 = [88.0,74.0,96.0,85.0]
list2 = [92.0,99.0,95.0,94.0]
list3 = [91.0,87.0,99.0,95.0]
list4 = [78.0,99.0,97.0,81.0]
list5 = [88.0,78.0,98.0,84.0]
list6 = [100.0,95.0,100.0,92.0]
X=np.array([list1,list2,list3,list4,list5,list6])
kmeans=KMeans(n_clusters=2).fit(X)
pred=kmeans.predict(X)
print(pred)