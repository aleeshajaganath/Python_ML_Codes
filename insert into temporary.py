dict = {'key1':'geeks'} 
#print("Current Dict is: ", dict) 
#
## using the subscript notation 
## Dictionary_Name[New_Key_Name] = New_Key_Value 
#dict['key2'] = 'for,ion'
#dict['key3'] = 'geeks'
#print("Updated Dict is: ", dict) 


str='SELECT `genere` FROM `movie_table` WHERE `movie_id` ='


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
    
    'collecting userid '
    
    userid=[656,583,
            707,696,
            761,0,
            797,0,
#  
          830,364
            ]; 
    i=0
    
    'sum of LL GEnres'
    
    diction = {} 
    
    
    usr=[]
#    cursor.execute ("select distinct userid from `collaborative_filtering` ORDER BY userid ASC ")
#    data = cursor.fetchall ()
    for r in range(0,len(userid),2):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            
            
    '_____________________________________________________________________________________________________' 

    '''sum all recommendations and storing in diction'''
    for r in range(0,len(userid),2):
     
#        Query3="SELECT sum(`recommendations`) FROM `collaborative_filtering` WHERE `userid`=%s"
        u=(userid[r])
        Query3='SELECT sum(`recommendations`)  FROM `collaborative_filtering` WHERE userid =%s and `filtered_recommendation`=0'
            
        cursor.execute(Query3,u)  


        
        data2 = cursor.fetchall()
        
   
        
        for row1 in data2:
        
            
            a=row1[0]
        
       
        
            dict1 = {userid[r]:a} 
    
            diction.update(dict1)



    '__________________________________________________________________________________'        
     
       
    'collecting movieid with genere from movie_table '    
    
     
#    mov=[]
    
    Query2= " SELECT `movie_id`,`genere` FROM `movie_table` "
    
    cursor.execute(Query2)  
        
    data2 = cursor.fetchall()
        
     
    for row1 in data2:
        
        a=row1[0]
        
        b=row1[1]
        
        dict1 = {a:b} 
    
        dict.update(dict1) 
    
#        print(dict)
        
     
      
    '______fetch userid_________'  
    for r in range(0,len(userid),2):
        
        print 'userid ',userid[r]
        
            
    
        '______fetch genre of movie_________' 
        
        
        Query2= " SELECT * FROM c where userid =%s"
       
        cursor.execute(Query2,656)  
        
        data2 = cursor.fetchall()
        
     
        for row1 in data2:
        
            
        
#            print 'm', row1[1]
            u=row1[0]
        
            m=row1[1]
        
            genre=dict[m].split(',')
        
            sum_gen=0
        
            for x in range(len(genre)):
            
            
#                print genre[x]
                Query3='SELECT recommendations FROM `collaborative_filtering` WHERE `genre`=%s and userid =%s and `filtered_recommendation`!=0 '
            
                gu=(genre[x],u)
                         
                cursor.execute(Query3,gu)  
        
                data3 = cursor.fetchall()
            
                for row3 in data3:
                
                    rcd=row3[0]
                
                    sum_gen=sum_gen+rcd
#                    print  rcd ,genre[x]
             
#            print sum_gen ,diction[userid[r]]
            
            sum_gen=sum_gen/float(diction[userid[r]])
             
#            print sum_gen 
#            p    
            qm='UPDATE temporary SET value=%s WHERE `Userid`=%s and `Movieid`=%s'
#           "
            
            sum_gen=sum_gen/float(diction[userid[r]])
            ar=(sum_gen,userid[r] ,m)
            cursor.execute(qm,ar)
            connection.commit()    
#            print 'sum_gen' ,sum_gen
            
             
   #
            
#            print m
                
                
                
            
            
        
#        recommendations=row1[1]
        
#    s='INSERT INTO `temporary (`userid`, `movieid`, `value`) VALUES ([value-1],[value-2],[value-3])'
#        
#   
#        
        
        
        
    
    
        
        
        
##        items.append(mov[i1+1])
##            
##            for r in range(0,len(usr[i1]),1):
##            
##                items.append()
#    
#        
#    
#    
#    i1=0
#    
#    for x in range(len(mov[i1+1])):
#    
#        u1=(mov[i1+1][x])
#        
#        print mov[i1+1][x]
#        
#        
                
                
except (pymysql.Error, pymysql.Warning) as e:
                print(e)