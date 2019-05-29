# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:42:13 2019

@author: user
"""

import pymysql
try:
    connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")

# prepare a cursor object using cursor() method
    cursor = connection.cursor()
    userid=[]
    cursor.execute ("select distinct userid from `collaborative_filtering` ORDER BY userid ASC ")
    data = cursor.fetchall ()
    for row in data:
            userid.append(row[0])
 
 
    a="select  * from `collaborative_filtering` where genre= %s "  
    for i in range(len(userid)):
    # userid[i] 
        u=(userid[i])
        cursor.execute("SELECT * FROM `collaborative_filtering` WHERE `genre`= %s ",u )  
        data1 = cursor.fetchall ()
        for row in data1:
            print row[0]
#cursor.execute(q, args)
         
    #connection.commit()

except (pymysql.Error, pymysql.Warning) as e:
                print(e)