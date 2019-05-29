# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:15:03 2019

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
 
import matplotlib 
matplotlib.rc('xtick', labelsize=15) 
matplotlib.rc('ytick', labelsize=15) 

# data to plot
n_groups = 4
Item_based = (
0.10,
0.16,
0.0,
0.0



)
Content_base = (
0.07,
0.07,
0.08,
0.09



)
Proposed_approach = (
0.56,
0.56,
0.56,
0.56



)
patterns = [   "/" ,"+", "-", "-", "O",  "*" ]
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4
 
rects1 = plt.bar(index, Item_based, bar_width,
alpha=opacity,hatch=patterns[3],
label='Item based filtering')
 
rects2 = plt.bar(index + bar_width,Content_base, bar_width,color='r',alpha=opacity,hatch=patterns[1],
label='Content based filtering')
rects = plt.bar(index + bar_width+bar_width, Proposed_approach, bar_width,alpha=opacity,hatch=patterns[0],color='g',
label='Proposed approach')
'''plt.xlabel('xlabel', fontsize=18)

fig.savefig('test.jpg')'''
plt.xlabel('Varying Similarity threshold', fontsize=18)
plt.ylabel('Recall', fontsize=16)

#plt.title('Scores by person')
plt.xticks(index + bar_width, ('.5', '.6', '.7', '.8'))
plt.legend()
 
#
plt.tight_layout()
plt.show()