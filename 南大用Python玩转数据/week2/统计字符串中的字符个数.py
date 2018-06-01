# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:25:56 2018

@author: Administrator
"""

'''
题目内容：
定义函数countchar()按字母表顺序统计字符串中所有出现的字母的个数（允许输入大写字符，并且计数时不区分大小写）。形如：
def countchar(str):
      ... ...
     return a list
if __name__ == "__main__":
     str = input()
     ... ...
     print(countchar(str))
'''

def countchar(str):
    result=[0]*26
    for i in str:
        if i.isalpha():
            #转化为ascii码
            index=ord(i.lower())-ord('a')
            result[index]+=1
    return result

if __name__ == "__main__":
     str = input()
     print(countchar(str))