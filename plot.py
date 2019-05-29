# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:20:59 2019

@author: user
"""

import matplotlib.pyplot as plt

fig = plt.figure()

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]

ax1 = fig.add_subplot(111)
for i in range(len(patterns)):
    ax1.bar(i, 3, color='red', edgecolor='black', hatch=patterns[i])


plt.show()