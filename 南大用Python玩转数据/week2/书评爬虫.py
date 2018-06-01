# -*- coding: utf-8 -*-
"""
Created on Thu May 31 22:54:00 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
import re
import time

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
    
#记录分数的数量
count1=0
#记录评论的数量
count2=0
#记录页码
index=1
#记录分数
Score=[]
#记录评论
Comment=[]

while(count1<=50 and count2<=50):
    url='https://book.douban.com/subject/1770782/comments/hot?p'+str(index)
    html=gethtml(url)
    soup=BeautifulSoup(html,'lxml')
    if(count1<50):
        pattern='<span class="user-stars allstar(.*?) rating"'
        score=re.findall(pattern,html)
        score=list(map(int,score))
        for i in score:
            Score.append(i)
            count1+=1
            if(count1==50):
                break
    if(count2<50):
        for i in soup.find_all('p','comment-content'):
            Comment.append(i.string)
            count2+=1
            if(count2==50):
                break
    if(count1==50 and count2==50):
        break
    time.sleep(5)# delay request from douban's robots.txt
    index+=1

#查看数量
print(len(Comment))
print(len(Score))

#打印第一句评论
print(Comment[0])
#打印均分
print(sum(Score)/len(Score))