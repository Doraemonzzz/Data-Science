# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 20:35:06 2018

@author: Administrator
"""

import requests
import re

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
    #注意换行符的处理
    pattern=re.compile(r'class="wsod_symbol">(.*?)</a>.*?<span.*?>(.*?)</span>.*?\n.*?<span.*?>(.*?)</span>')
    dji_list_in_text=re.findall(pattern,text)
    dji_list = []

    for i in dji_list_in_text:
        dji_list.append([i[0],i[1],float(i[2])])
    return dji_list

url='https://money.cnn.com/data/dow30/'
dji_list=getdata(url)

with open('dji_list.txt',mode='w') as file:
    file.write('column1,column2,column3\n')
    for i in dji_list:
        text=','.join(map(str,i))+'\n'
        file.write(text)