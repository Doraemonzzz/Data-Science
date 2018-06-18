# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:28:56 2018

@author: Administrator
"""

import pandas as pd
music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N'\
Roses","Don't Cry"),("Metallica","Nothing Else Matters")]

dic={'singer':[],'song_name':[]}

for i in music_data:
    dic['singer'].append(i[0])
    dic['song_name'].append(i[1])
    
frame=pd.DataFrame(dic,index=range(1,5))

print(frame)
