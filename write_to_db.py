# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:48:08 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 00:15:14 2019

@author: user
"""
import pymysql
import requests
"encoding='utf8')"
import bs4

connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "movie_lense")
#pbz = open("G:\movie_lense\ml-100k\u.data.txt","w") 
# prepare a cursor object using cursor() method
cursor = connection.cursor()
#try:
with open("G:\movie_lense\ml-100k\u1.base.txt","r")  as f:
    lines = f.readlines()
   # print "\n",lines
    st='https://www.imdb.com'
    
    for l in lines[5:]:
          v= l.split("\t")
          #print (v[0]+v[1]+v[2])
          
#          res= requests.get(v[1])
#
#          soup= bs4.BeautifulSoup(res.text,'lxml')
#          My_table = soup.find('table',{'class':'cast_list'})
#          if My_table is None:
#              print 'Something happened'
#             # pbz.write(v[0]+"|"+v[1])
#              
#              continue
#          links= My_table.find_all('img')
          
#
#          cast=[]
#          for link in links:
#              cast.append(link.get('title'))
        
          try:
              
                insert_tuple = (v[0],v[1],v[2])
                #print(insert_tuple)
                query = "INSERT INTO  rating_table1 values(%s,%s,%s) "
                i=cursor.execute(query,insert_tuple)
                print i
                
                #cursor.executemany("""INSERT INTO db (userid,FI,sim) VALUES(%s,%s,%s)""",lst)
                connection.commit()

          except (pymysql.Error, pymysql.Warning) as e:
                print(e)
#          try:
#              file1 = open("cast2.txt","w") 
#              for i in range(len(cast)):
#              #file1.write(printinfo.encode('utf8') + '\n')
#                  file1.write(v[0]+"|"+cast[i]+"\n") 
#              #print(v[0]+"|"+cast[i]+"\n") 
#          finally:
#               file1.close()
#except :
#       print (v[0]+"|"+cast[i]+"\n") 
#       
#   
#file1.close()
#print(soup.get_text())
#body =soup.body
#div=soup.div

#for div in  body.find_all('div'):
#    print(div.id)


