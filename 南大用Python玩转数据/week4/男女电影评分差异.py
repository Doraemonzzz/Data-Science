# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:22:02 2018

@author: Administrator
"""

import pandas as pd

rate=pd.read_table('ml-100k/u.data',sep='\t',names=['user','item','rating','timestamp'])
user=pd.read_table('ml-100k/u.user',sep='|',names=['user','age','gender','occupation','zip code'])

rawdata=pd.merge(rate,user,on='user',how='inner')

data=rawdata.loc[:,['rating','gender','user']]
groupdata=data.groupby(['user','gender']).mean()

male=groupdata.query("gender==['F']")
female=groupdata.query("gender==['M']")

print(male.std())
print(female.std())

