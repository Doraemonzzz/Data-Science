# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:50:31 2018

@author: Administrator
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    result=[]
    if(songs[0][2]>max_size):
        return result
    else:
        result.append(songs[0][0])
        #记录重量
        size=songs[0][2]
        while(1):
            minsize=max_size
            name=''
            #找到重量最小的
            for i in songs:
                if i[0] not in result and i[2]<minsize:
                    minsize=i[2]
                    name=i[0]
            if(minsize+size<=max_size):
                result.append(name)
                size+=minsize
            else:
                break
    return result

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 12.2
print(song_playlist(songs, max_size))

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 11
print(song_playlist(songs, max_size))