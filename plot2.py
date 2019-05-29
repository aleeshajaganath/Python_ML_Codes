# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:39:06 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

data = [[.5, .6, .7, .8],
  ]

X = np.arange(4)
plt.bar(X + 0.00, data[0], color = 'w', width = 0.425,hatch='*',
label='Content based filtering')
plt.xticks(X , ('A', 'B', 'C', 'D', 'D'))
#plt.bar(X + 0.425, data[1], color = 'w',hatch='.', width = 0.425)
#plt.bar(X + 0.50, data[2], color = 'r', width = 0.425)

plt.show()