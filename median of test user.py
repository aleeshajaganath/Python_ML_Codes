# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:19:38 2019

@author: user
"""

'___________find median using threshold________'

Threshold=.7
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:32:13 2019

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
#            830,364
            ]; 
    i=0
    usr=[]
#    cursor.execute ("select distinct userid from `collaborative_filtering` ORDER BY userid ASC ")
#    data = cursor.fetchall ()
    for r in range(0,len(userid),2):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            usr.append(userid[r])
            q='SELECT count(rating) FROM `rating_table` WHERE `userid`=%s '
          
            cursor.execute(q,u)  
            data1 = cursor.fetchall ()
            items=[]
            for row1 in data1:
                c=row1[0]
                c=Threshold*c
                items.append(c)
                usr.append(c)
    
#            if len(userid[i]) == 0:
#                print userid[i]
#                del userid[i-1]
#                del userid[i]
#            else:
#                userid.append(items)
#                i=i+1
    
    
    w=[]
    for r in range(0,len(userid),2):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            usr.append(userid[r])
            q='SELECT rating FROM `rating_table` WHERE `userid`=%s order by rating'
          
            cursor.execute(q,u)  
            data1 = cursor.fetchall ()
            items=[]
            for row1 in data1:
               
                items.append(row1[0])
                
            c=items[int(usr[r+1])]
            w.append(c)
            
    for r in range(0,len(userid),2):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            usr.append(userid[r])
            q='SELECT rating FROM `rating_table` WHERE `userid`=%s order by rating'
          
            cursor.execute(q,u)  
            data1 = cursor.fetchall ()
            items=[]
            '_______storing all the items in asc______________'
            for row1 in data1:
               
                items.append(row1[0])
                
            c=items[int(usr[r+1])]
            
            q='SELECT movieid,rate FROM `temporary` WHERE `userid`=%s '
          
            cursor.execute(q,u)  
            data2 = cursor.fetchall ()
#            items1=[]
            
            
            for row2 in data2:
               
                b=row2[0]#movieid,rating
                c1=row2[1]#,rating
                if c1>=c:
                    
                    a=1
                    
                    d=(a,userid[r],b)
            
                    sx='UPDATE `temporary` SET combined_prediction3=%s  WHERE userid =%s and `movieid`=%s'
 
                    cursor.execute(sx,d)
                    
                    data3 = cursor.fetchall ()
                    
#                items.append(c)
#                usr.append(c)
            connection.commit()
## 
#            
#    a= "SELECT SU FROM `user1ratingsimilarityuser2_2` WHERE `FU`=%s and `SIMILARITY`>=.5 " 
#      
#    Query1= "SELECT movieid FROM `content based filtering` WHERE `userid`=%s and movieid>=%s" 
#    'selecting 1st user FU and SU'
#    
#    for i in range(0,len(usr),2):
#    # userid[i] 
#        u=(usr[i])
#        cursor.execute(a,u )  
#        data1 = cursor.fetchall ()
#        similar_user=[]
#        
#        ' storing similar user for usr[i] '
#        
#        for row in data1:
#            similar_user.append(row[0])
#            #print row[0]
#        
#        
#        ' select all movies recommendedto user '
#        
#        Queryb= "SELECT rating FROM rating_table WHERE userid =%s and movieid=%s" 
#       
#        add=[]
#        print ' user',usr[i]
#        for m in range(len(usr[i+1])):
#          sum=0
#          add.append(usr[i+1][m])
#          'all similar user'
#         
#          sim_c=0
#          for s in range(len(similar_user)):
#            #sum=0
#            #print 'similar user' ,similar_user[s],'movie',usr[i+1][m]
#            d=(similar_user[s],usr[i+1][m])
#            cursor.execute(Queryb,d ) 
#            data2 = cursor.fetchall ()
#            for row2 in data2:
#                #print 'similar user' ,similar_user[s],'movie',usr[i+1][m]
#                print row2[0]
#                sum=sum+row2[0]
#                if row2[0]!=0:
#                    sim_c=sim_c+1
#           
#          if sum!=0:    
#                #
#                print'sum is ',sum,'similar user' ,similar_user[s]
#                qm= " UPDATE `content based filtering` SET `similar_user_avg`=%s WHERE `userid`=%s and `movieid`=%s"
#                sum=sum/float(sim_c)
#                argsm=(sum,usr[i],usr[i+1][m])
##                cursor.execute(qm, argsm)
##                connection.commit()
##            
##            cursor.execute(q, args)
#         
#    connection.commit()

except (pymysql.Error, pymysql.Warning) as e:
                print(e)