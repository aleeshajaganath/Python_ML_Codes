# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:59:36 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:19:38 2019

@author: user
"""

'___________find median using threshold________'

Threshold=.6
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:32:13 2019

@author: user
"""


import pymysql
try:
    connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")

# prepare a cursor object using cursor() method
    cursor = connection.cursor()
    userid=[656,583,
            707,696,
            761,0,
            797,0,
#           
             830,364
            ]; 
    i=0

    'SELECT `userid`, `movieid`, `rating` FROM `matrix_factorization` WHERE 1'
    
    
    for r in range(0,len(userid)):
#            userid.append(row[0])
#            i=i+1
        
        u=(userid[r])
           
    
        q='SELECT  `userid`, `movieid`, `rating` FROM `matrix_factorization` WHERE userid=%s  '
        qa=(userid[r]) 
        cursor.execute(q,u)  
        data1 = cursor.fetchall ()
        items=[]
        for row1 in data1:
               # a=row1[2]
                print row1[0]
                matrix_rate=row1[2]
                movieid=row1[1]
                userid=row1[0]
                d=(matrix_rate,movieid,userid)
                 
                s1='UPDATE `temporary` SET matrix_rate=%s  WHERE  `movieid`=%s and userid=%s'
            
#                print row1[2],row1[1],row1[0]
                # 
                cursor.execute(s1,d)  
                data1 = cursor.fetchall ()
#                items.append(c)
#                usr.append(c)
    connection.commit()
except (pymysql.Error, pymysql.Warning) as e:
                print(e)