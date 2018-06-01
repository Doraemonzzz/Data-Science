# -*- coding: utf-8 -*-
"""
Created on Thu May 31 23:30:47 2018

@author: Administrator
"""

'''
1. 使用以下语句存储一个字符串：
  str = 'My moral standing  is: 0.98765'
将其中的数字字符串转换成浮点数并输出。 
'''
str = 'My moral standing  is: 0.98765'

start=str.find(':')

num=float(str[start+1:])

print(num)

'''
输入一个字符串“I like Python very much 2333 because Python is very cute 666.”，
判别该字符串中数字字符和单词的个数，
并将第一次出现的Python替换成你偶像的名字并输出新字符串。
'''

str='I like Python very much 2333 because Python is very cute 666.'
result=str.split(' ')

num1=num2=0
for i in result:
    try:
        float(i)
        num1+=1
    except:
        num2+=1
        
print("数字有{0:d}个，单词有{1:d}个".format(num1,num2))

a=str.find("Python")
ans=str[:a]+"China"+str[a+6:]
print(ans)