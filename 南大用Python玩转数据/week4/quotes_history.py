# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:08:03 2018

@author: Administrator
"""

import requests
import re
import json

def gethtml(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        pass

def getdata(url):
    text=gethtml(url)
    quotes = []
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', text)
    if m:
        quotes=json.loads(m[0])
        quotes=quotes[::-1]
    #'type'是多余数据
    result=[i for i in quotes if 'type' not in i]
    return result

url='https://finance.yahoo.com/quote/AXP/history?p=AXP'
quotes=getdata(url)

with open('quotes.txt',mode='w') as file:
    file.write(','.join(quotes[0].keys())+'\n')
    for i in quotes:
        text=','.join(map(str,i.values()))+'\n'
        file.write(text)

