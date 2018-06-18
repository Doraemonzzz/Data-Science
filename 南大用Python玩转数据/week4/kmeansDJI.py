# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 21:57:18 2018

@author: Administrator
"""

# 本程序有一定的网络负载，可不运行程序根据结果理解程序
import requests
import re
import json
import pandas as pd
from sklearn.cluster import KMeans 
import numpy as np
 
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

def create_df(stock_code):
    quotes = retrieve_quotes_historical(stock_code)
    list1 = ['close','date','high','low','open','volume']
    df_totalvolume = pd.DataFrame(quotes,columns=list1)
    # 用数据的平均值代替数据中的空值（NaN）
    df_totalvolume = df_totalvolume.fillna(df_totalvolume.mean())
    return df_totalvolume

listDji = ['MMM','AXP','AAPL','BA','CAT','CVX','CSCO','KO','DIS','DD']
listTemp = [0] * len(listDji)
for i in range(len(listTemp)):
    listTemp[i] = create_df(listDji[i]).close
status = [0] * len(listDji)
for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
# 简单处理某一只或几只股票数据没有获得（值为[])的问题，删掉此数据
for i in range(len(status)):
    if len(status[i]) == 0:
             status.pop(i)
             break
kmeans = KMeans(n_clusters = 3).fit(status)
pred=kmeans.predict(status)
print(pred)