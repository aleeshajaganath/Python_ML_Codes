# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:19:12 2019

@author: user
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('.5', '.6', '.7', '.8', '.9')
y_pos = np.arange(len(objects))
performance = [1,3,5,4,2]
 
plt.bar(y_pos, performance, alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()