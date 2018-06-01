# -*- coding: utf-8 -*-
"""
Created on Thu May 31 21:28:37 2018

@author: Administrator
"""
#获取http://money.cnn.com/data/dow30/股票信息

import requests
from bs4 import BeautifulSoup

def gethtml(url):
    try:
        r=requests.get(url)
        #查看状态码
        r.raise_for_status()
        #解码
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
  
#解析数据
def getinformation(url):
    html=gethtml(url)
    soup=BeautifulSoup(html,'html.parser')
    #观察网页信息
    a=soup.find_all('tr')
    stock=[]
    for i in a:
        temp=[]
        try:
            temp.append(i.find('a').string)
            for j in i.find_all('span'):
                #防止公司简称和全称一致
                if(len(temp)>1):
                    if j.string not in temp and j.string!=None:
                        temp.append(j.string)
                else:
                    temp.append(j.string)
            for j in i.find_all('td'):
                if j.string not in temp and j.string!=None:
                    temp.append(j.string)
        except:
            continue
        stock.append(temp)
    return stock

#格式化输出
def show(info):
    tplt = "{:<10}\t{:10}\t{:20}\t{:10}\t{:10}\t{:10}\t{:10}\t{:10}\t"
    print(tplt.format("number","Abbreviation","Company","Price","Change","% Change","Volume","YTD change"))
    for i in range(len(info)):
        print(tplt.format(i+1,info[i][0],info[i][1],info[i][2],info[i][6],info[i][3],info[i][4],info[i][5]))

def main():
    url="http://money.cnn.com/data/dow30/"
    info=getinformation(url)
    show(info)
    
main()