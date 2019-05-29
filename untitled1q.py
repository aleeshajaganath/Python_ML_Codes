# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:45:32 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:39:06 2019

@author: user
"""
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt')
import numpy as np
import matplotlib.pyplot as plt

data = [[5., 25., 50., 20.],
  [4., 23., 51., 17.],
  [6., 22., 52., 19.]]

X = np.arange(4)
plt.bar(X + 0.00, data[0], color = 'w', width = 0.425,label='Content based filtering')
#plt.bar(X + 0.425, data[1], color = 'w',hatch='.', width = 0.425)
#plt.bar(X + 0.50, data[2], color = 'r', width = 0.425)

plt.show()