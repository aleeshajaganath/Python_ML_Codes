# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:21:21 2019

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
#            830,364
            ]; 
    i=0
    usr=[]
    data = cursor.fetchall ()
    for r in range(0,len(userid),2):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            usr.append(userid[r])
            s='SELECT `userid`,`movieid`,`rate` FROM `c` WHERE `userid`=%s '
#            q='SELECT count(rating) FROM `rating_table`  '
          
            cursor.execute(s,u)  
            data1 = cursor.fetchall ()
            items=[]
            for row1 in data1:
                
                c=(row1[2],row1[1],row1[0])
                 
                s1='UPDATE `temporary` SET rate`=%s  WHERE `Userid =%s and `Movieid`=%s'
            
                print row1[2],row1[1],row1[0]
                 
            
#                cursor.execute(s,c)  
#                data1 = cursor.fetchall ()
#                items.append(c)
#                usr.append(c)
#    
    
   
##            

except (pymysql.Error, pymysql.Warning) as e:
                print(e)