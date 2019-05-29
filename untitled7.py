# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:44:30 2019

@author: user
"""
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt')
import numpy as np
import matplotlib.pyplot as plt
patterns = [ "/"   ,  "*", "o", "O", ".", ]
data = [[.5, .6, .7,.8,.9]]

color_list = ['b', 'g', 'r']
gap = .3
for i, row in enumerate(data):
  X = np.arange(len(row))
  plt.bar(X + 0 * gap, row,
    width = gap,hatch=patterns[0],
    color = 'g')
plt.xticks(X + 0 * gap, ('A', 'B', 'C', 'D', 'D'))
plt.show()