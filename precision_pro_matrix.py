# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:29:01 2019

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
n_groups =3
Item_based = (0.26,0.22,0.23)
Content_base = (0.56, 0.30,0.28)
#Proposed_approach = (0.31,0.31, 0.31, 0.31)
patterns = [   "/" ,"+", "-", "-", "O",  "*" ]
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4
 
rects1 = plt.bar(index, Item_based, bar_width,
alpha=opacity,hatch=patterns[3],
label='Matrix Factorization')
 
rects2 = plt.bar(index + bar_width,Content_base, bar_width,color='r',alpha=opacity,hatch=patterns[1],
label='Proposed Approach')

'''plt.xlabel('xlabel', fontsize=18)

fig.savefig('test.jpg')'''

plt.xlabel('No: of Recommendations', fontsize=18)
plt.ylabel('Precision', fontsize=16)

#plt.title('Scores by person')
plt.xticks(index + bar_width, ('6', '15', '30'))
plt.legend()
#
plt.tight_layout()
plt.show()