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
    cursor.execute ("SELECT distinct `genere` FROM `genere` WHERE 1 ")
    data = cursor.fetchall ()
    for row in data:
        genere.append(row[0])
        
    movie=[]
    cursor.execute ("SELECT distinct userid FROM item_movie WHERE 1 ")
    data = cursor.fetchall ()
    for row in data:
        movie.append(row[0])    
    
   
    
   
    gen=0
    q1="SELECT * FROM `item_movie` where cast= %s"
    d1=(genere[gen])
    q="SELECT * FROM `item_movie1` where userid= %s and cast = %s"
    
    cursor.execute (q1,d1)
    data = cursor.fetchall ()
    
    for i in range(len(movie)):
        for j in range(len(genere)):
#    if data is not None:
#         sum=0
#         q1="SELECT * FROM `item_movie` where cast= %s"
#         d1=(genere[gen])
         
         mov=0
         d=(movie[i],genere[j])
         cursor.execute (q,d)
         count=0
         data1 = cursor.fetchall ()
         a=0
         b=0
         for row in data1:
             print row[0],row[1],row[2]
             a=row[0]
             b=row[2]
             count=count+1
         if count!=0: 
             qm= " INSERT INTO `collaborative_filtering`(`userid`, `recommendations`, `genre`) VALUES(%s,%s,%s)"
             argsm=(movie[i],count,genere[j])
             cursor.execute(qm, argsm)
             connection.commit()
        
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