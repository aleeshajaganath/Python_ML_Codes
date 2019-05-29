# -*- coding: utf-8 -*-


''' Inserting  into the temporary table with combined_prediction'''



import pymysql
try:
    connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")

     
    cursor = connection.cursor()
            
    Query2= "SELECT * FROM `c` WHERE 1" 
    
     
    Query3= "SELECT `value1` FROM `temporary` WHERE `userid`=%s and `movieid`=%s" 
    
    cursor.execute(Query2)  
        
    data2 = cursor.fetchall()
    
    for row1 in data2:
         
       
        a=row1[0]
         
        
        
        b=row1[1]
        
         
#        print a,b
        
        c1= row1[2]
        
        arg=(a,b)
        cursor.execute(Query3,arg)       
        data3 = cursor.fetchall()
        
         
        for row3 in data3:
             
              c2= row3[0]
              
              c3=(c1+c2)/2
               
#              print c1,c2
              print c3
              'UPDATE `temporary` SET `userid`=[value-1],`movieid`=[value-2]'
              'value1`=[value-3],=[value-4],`rate`=[value-5] WHERE 1'
        qm='UPDATE temporary SET `combined_prediction1`=%s WHERE `Userid`=%s and `Movieid`=%s'
#           "
            
            
        #sum_gen=sum_gen/float(diction[userid[r]])
        
        ar=(c3 ,a,b)
        
        cursor.execute(qm,ar)
        
        connection.commit()    
    
   
                
except (pymysql.Error, pymysql.Warning) as e:
                print(e)