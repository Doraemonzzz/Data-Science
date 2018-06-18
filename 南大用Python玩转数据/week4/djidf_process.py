# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:43:52 2018

@author: Administrator
"""

import pandas as pd
from datetime import date
djidf=pd.read_table('dji_list.txt',sep=',')
quotes=pd.read_table('quotes.txt',sep=',')

cols=['code','name','lasttrade']
djidf.columns=cols
djidf.index=range(1,len(djidf)+1)

#将quotes的时间转换
Date=[]
Month=[]
for i in range(len(quotes)):
    x=date.fromtimestamp(quotes.loc[i,'date'])
    y=date.strftime(x,'%Y-%m-%d')
    Date.append(y)
    month=int(y.split('-')[1])
    Month.append(month)

quotes.index=Date
quotes=quotes.drop('date',axis=1)
quotes['month']=Month

print(djidf)
print(quotes)

