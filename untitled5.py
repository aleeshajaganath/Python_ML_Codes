# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:49:58 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:25:16 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 3

Content_base = (0.14, 0.15,0.12)

patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.1525
opacity = 0.2
 
#
rects1 = plt.bar(index,Content_base, bar_width,alpha=opacity,hatch=patterns[3],
label='Item based filtering')
 
rects2 = plt.bar(index ,Content_base, bar_width,
alpha=opacity,
label='recommendations for similarity threshold = 0.6')
#
rects = plt.bar(index + bar_width+bar_width, Content_base, bar_width,
alpha=opacity,hatch=patterns[0],label='Proposed approach')
 
plt.xlabel('No: of Recommendations')
plt.ylabel('Precision')
#plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C'))
plt.legend()
 
#plt.tight_layout()
plt.show()