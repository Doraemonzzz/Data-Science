# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:08:22 2018

@author: Administrator
"""

s_dict={}
s = "我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧 ， 重要 事情 说 三遍 ！"
s1=s.split(' ')

for i in s1:
    if i not in "，。！“”":
        if i not in s_dict.keys():
            s_dict[i]=1
        else:
            s_dict[i]+=1
            
print(s_dict)
        