# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:57:59 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:25:16 2019

@author: user
"""
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt')
import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 4
Item_based = (0.05,0.05,0.08, 0.06)
Content_base = (0.07, 0.07,0.08, 0.09)
Proposed_approach = (0.31,0.31, 0.31, 0.31)
patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4
 
rects1 = plt.bar(index, Item_based, bar_width,
alpha=opacity,hatch=patterns[3],
label='Item based filtering')
 
rects2 = plt.bar(index + bar_width,Content_base, bar_width,
alpha=opacity,hatch=patterns[1],
label='Content based filtering')
rects = plt.bar(index + bar_width+bar_width, Proposed_approach, bar_width,alpha=opacity,hatch=patterns[0],color='g',
label='Proposed approach')
 
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()
plt.rc('xtick', labelsize=18) 
plt.rc('ytick', labelsize=18) 
plt.rc('xlabel', labelsize=18) 
plt.rc('ylabel', labelsize=18) 
#
plt.tight_layout()
plt.show()