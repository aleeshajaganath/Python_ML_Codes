# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:36:10 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:38:33 2019

@author: user
"""

import pymysql

# open a database connection
connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")
cursor = connection.cursor()
s="SELECT distinct `movieid` FROM  `rating_table` ORDER BY `movieid` ASC"
movie=[]
try:
              
                insert_tuple = ()
               
                print(insert_tuple)
                #print(insert_tuple)
#                query = "INSERT INTO  rating_table1 values(%s,%s,%s) "
#                i=cursor.execute(query,insert_tuple)
#                print i
#                
                #
                cursor.execute(s)
                result = cursor.fetchall()
                for row in result:
                    
                   # print(row[0])
                    movie.append(row[0])
               

          
except (pymysql.Error, pymysql.Warning) as e:
                print(e)
#s1="SELECT distinct `userid` FROM `rating_table` ORDER BY `userid` ASC"
#user=[]
#try:
#              
#                insert_tuple = ()
#               
#                #print(insert_tuple)
#                #print(insert_tuple)
##                query = "INSERT INTO  rating_table1 values(%s,%s,%s) "
##                i=cursor.execute(query,insert_tuple)
##                print i
##                
#                #
#                cursor.execute(s1)
#                result = cursor.fetchall()
#                for row in result:
#                    
#                   # print(row[0])
#                    user.append(row[0])
#               
#
#          
#except (pymysql.Error, pymysql.Warning) as e:
#                print(e)
#
#
#
#
##for l in range(0,80):
##     movie.append(row[0])
#
#j=0
#with open("dob6.csv","r")  as f:
#          lines = f.readlines()
#          try:
#              
#              print("_______")
##              print(movie[j])
##              j=j+1
#              
#              for l in lines[0:]:
#        
#                    v= l.split("|")
#                   
#                    for i in range(0,len( movie)):
#                       
##                        print(movie[i])
##                        print(v[i])
#                        insert_tuple = (user[j],movie[i],v[i])
#                        print(insert_tuple)
#                        
#                        query = "INSERT INTO  r6  values(%s,%s,%s) "              
#                        i=cursor.execute(query,insert_tuple)
#                        connection.commit()
#                        
#                    j=j+1    
#               
#                #
#                #print(insert_tuple)
#                #print(insert_tuple)
##               
##                print i
##                
#                #cursor.executemany("""INSERT INTO db (userid,FI,sim) VALUES(%s,%s,%s)""",lst)
#              
#
#          except (pymysql.Error, pymysql.Warning) as e:
#                print(e)