# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:32:55 2018

@author: Administrator
"""

import pandas as pd

dic={'name':['Mayue','Lilin','Wuyun'],'pay':[3000,4500,8000]}
a=pd.DataFrame(dic)
#print(a)

#添加列
a['tax']=[0.05,0.05,1]
#print(a)

#添加行
a.loc[5]= {'name': 'Liuxi', 'pay': 5000, 'tax': 0.05}
#print(a)

#删除对象元素，不改变原始数据
a.drop(5)
#print(a)

#删除列
print(a.drop('tax', axis = 1))