# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:38:47 2019

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
            830,364]; 
    i=0
    usr=[]
#    cursor.execute ("select distinct userid from `collaborative_filtering` ORDER BY userid ASC ")
#    data = cursor.fetchall ()
    for r in range(0,len(userid),2):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            
            Query2= "SELECT `cast` FROM `item_movie` WHERE `movieid``=%s " 
    mov=[867]
    i1=0
    for x in range(len(mov[i1+1])):
        u1=(mov[i1+1][x])
        print mov[i1+1][x]
        cursor.execute(Query2,u1)  
        data2 = cursor.fetchall()
        items=[]
        
        for row1 in data2:
            items.append(mov[i1+1])
            for r in range(0,len(usr[i1]),1):
                items.append(row1[0])
                
                
except (pymysql.Error, pymysql.Warning) as e:
                print(e)