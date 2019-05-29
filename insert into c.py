# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:38:47 2019

@author: user
"""

diction = {} 
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


    item=[]
    Query2="SELECT * FROM `temporary` ORDER BY `Userid` ASC  "
    
     
    for r in range(0,len(userid),2):
     
#        Query3="SELECT sum(`recommendations`) FROM `collaborative_filtering` WHERE `userid`=%s"
        u=(userid[r])
        Query3='SELECT sum(`recommendations`)  FROM `collaborative_filtering` WHERE userid =%s  '
            
        cursor.execute(Query3,u)  


        
        data2 = cursor.fetchall()
        
   
        
        for row1 in data2:
        
            
            a=row1[0]
        
       
        
            dict1 = {userid[r]:a} 
    
            diction.update(dict1)
            
#        items.append(mov[i1+1])
            
          
                
                
except (pymysql.Error, pymysql.Warning) as e:
                print(e)