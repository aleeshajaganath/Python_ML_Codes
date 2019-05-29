# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:20:47 2019

@author: user
"""


Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
t=['Name','Geeks','Geeks']
for i in range(len(t)):
       try:
        if Dict[t[i]] is not None:
            print Dict[t[i]]
       except:
            print 'error '   