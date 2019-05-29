# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:51:00 2019

@author: user
"""

import pymysql

connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")
#pbz = open("G:\movie_lense\ml-100k\u.data.txt","w") 
# prepare a cursor object using cursor() method


#cursor = connection.cursor()
#cursor.execute ("select distinct `movieid` from rating_table  ORDER BY `movieid` ASC ")
#data = cursor.fetchall ()
#for row in data:
#    print row[0]
try:
    
    
              
                
    i=0
    genere=[]
    cursor = connection.cursor()
    
    user=[]
    cursor.execute ("SELECT distinct userid FROM collaborative_filtering WHERE 1 ")
    data = cursor.fetchall ()
    for row in data:
        user.append(row[0])    
    
   
    
   
#    gen=0
#    q1="SELECT * FROM `item_movie` where cast= %s"
#    d1=(genere[gen])
    q="SELECT * FROM collaborative_filtering where userid= %s "
#    d=(user[i])
#    cursor.execute (q,d)
#    data = cursor.fetchall ()
#   
    for i in range(len(user)):
        
#         sum=0
#         q1="SELECT * FROM `item_movie` where cast= %s"
#         d1=(genere[gen])
         
        
         d=(user[i])
         cursor.execute (q,d)
         count=0
         data1 = cursor.fetchall ()
         a=0
         b=0
         
         temp=[]
         for row in data1:
             temp.append(row[1])
             temp.append(row[2])
             #print row[0],row[1],row[2]
         c=0
         print"___"
         for i1 in range(0,len(temp),2):
             c=temp[i1]+c
             #print temp[i1]
         print c    
         for i1 in range(0,len(temp),2):
            # print float(temp[i1]/float(c))
             qm="update collaborative_filtering set percentage=%s where userid=%s and genre=%s"
             ar=(float(temp[i1])/float(c) ,user[i],temp[i1+1])
             cursor.execute(qm,ar)
             connection.commit()
#             a=row[0]
#             b=row[2]
#             count=count+1
#         if count!=0: 
#             qm= " INSERT INTO `collaborative_filtering`(`userid`, `recommendations`, `genre`) VALUES(%s,%s,%s)"
#             argsm=(movie[i],count,genere[j])
#             cursor.execute(qm, argsm)
#             connection.commit()
#        
#    for i in range(len(m)):
#        print m[i]
#        q="INSERT INTO genere (genere) VALUES(%s)"
#        args=(m[i])
#        cursor.execute(q, args)
#        connection.commit()
#                
                #cursor.executemany("""INSERT INTO db (userid,FI,sim) VALUES(%s,%s,%s)""",lst)
             #connection.commit()

except (pymysql.Error, pymysql.Warning) as e:
                print(e)