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
    
    
              
                
    m=[]
    cursor = connection.cursor()
    cursor.execute ("SELECT distinct `genere` FROM `movie_table` WHERE 1 ")
    data = cursor.fetchall ()
    for row in data:
        m1=row[0].split(",")
        for i in range(len(m1)):
            m.append(m1[i])
            
    for i in range(len(m)):
        print m[i]
        q="INSERT INTO genere (genere) VALUES(%s)"
        args=(m[i])
        cursor.execute(q, args)
        connection.commit()
                
                #cursor.executemany("""INSERT INTO db (userid,FI,sim) VALUES(%s,%s,%s)""",lst)
             #connection.commit()

except (pymysql.Error, pymysql.Warning) as e:
                print(e)