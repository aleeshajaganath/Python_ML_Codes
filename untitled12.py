# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:50:05 2019

@author: user
"""
import pymysql

connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")

# prepare a cursor object using cursor() method
cursor = connection.cursor()

cursor.execute ("select distinct `movieid` from rating_table  ORDER BY `movieid` ASC ")
data = cursor.fetchall ()
q="INSERT INTO `collaborative_filtering`(`userid`, `recommendations`, `genre`) VALUES(%s,%s,%s)"
         
a=1
s="drama"
args=(a,a,s)
 
  
      
cursor.execute(q, args)
         
connection.commit()

try:
    q="INSERT INTO `collaborative_filtering`(`userid`, `recommendations`, `genre`) VALUES(%s,%s,%s)"
         
    a=1
    s="drama"
    args=(a,a,s)
 
  
      
    cursor.execute(q, args)
         
    connection.commit()
    
    
except (pymysql.Error, pymysql.Warning) as e:
                print(e)