dict = {'key1':'geeks'} 
#print("Current Dict is: ", dict) 
#
## using the subscript notation 
## Dictionary_Name[New_Key_Name] = New_Key_Value 
#dict['key2'] = 'for,ion'
#dict['key3'] = 'geeks'
#print("Updated Dict is: ", dict) 


str='SELECT `genere` FROM `movie_table` WHERE `movie_id` ='





import pymysql
try:
    connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "myopinio_ver1")

# prepare a cursor object using cursor() method
    cursor = connection.cursor()
    
    'collecting userid '
    
    userid=[656,#583,
            707,#696,
            761,#0,
            797,#0,
#            830,364
            ]; 
    i=0
    
    'sum of LL GEnres'
    
    
    
    
    
    
    '______________________users average___________________________________________ '
    
    
    str='select avg(rating) from rating_table where userid=%s'
    
    diction = {} 
    
    
    usr_avg=[]
    
   
    
    for r in range(0,len(userid)):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r])
            cursor.execute (str,u)
    
            data = cursor.fetchall ()
            
            for row in data:
             
                usr_avg.append(row[0])
                
      
        
        
        
    str='select movieid,rating from rating_table where userid=%s and rating>=%s'
    
    diction = {} 
    
    
#    usr_movies=[]
    
    for r in range(0,len(userid)):
#            userid.append(row[0])
#            i=i+1
        
            u=(userid[r],usr_avg[r])
            cursor.execute (str,u)
    
            data = cursor.fetchall ()
            
            for row in data:
             
                usr_movies=row[0]
                
                str_movie='select genere  FROM `movie_table` where movie_id=%s'
                u1=(usr_movies)
                cursor.execute (str_movie,u1)
    
                data1 = cursor.fetchall ()
                
                for row1 in data1:
                    genere=row1[0].split(',')
                    
                    for i in range(0,len(genere) ):
                        qm='UPDATE collaborative_filtering SET filtered_recommendation=%s WHERE `Userid`=%s and `genre`=%s'
                        p=1
                        ar=(1,userid[r] ,genere[i])
                        cursor.execute(qm,ar)
                        connection.commit() 
                    
                    
                    
                    
                    
                     
                    
                    
                  
        
#    1n 
#            p    
#            qm='UPDATE `c` SET `weight`=%s WHERE `Userid`=%s and `Movieid`=%s'
##           "
#            
#            sum_gen=sum_gen/float(diction[userid[r]])
#            ar=(userid[r] ,m,sum_gen)
#            cursor.execute(qm,ar)
#            connection.commit()    
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