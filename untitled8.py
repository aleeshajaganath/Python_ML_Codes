# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:26:34 2019

@author: user
"""

import numpy as np
from numpy import linalg as LA
A = np.array([[2.5, 1. , 4. ,0,0],
       [3. , 0. , 3.,0,0 ],
       [2. , 3.5, 5.,0,0 ],
       [4. , 3. , 0.,0,0 ],
       [5. , 4.5, 0. ,0,0]])
w, v = LA.eig(A)
print(w)