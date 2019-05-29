# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 00:15:14 2019

@author: user
"""
import pymysql
import requests
"encoding='utf8')"
import bs4

connection = pymysql.connect(host = "localhost",port=3306,user = "root", passwd = "", db = "projectw")
pbz = open("url_id_pbz3.txt","w") 
# prepare a cursor object using cursor() method
cursor = connection.cursor()
#try:
with open("url_id_2.txt","r")  as f:
    lines = f.readlines()
   # print "\n",lines
    st='https://www.imdb.com'
    
    for l in lines[0:]:
          v= l.split("|")
          print (v[0])
          
          res= requests.get(v[1])

          soup= bs4.BeautifulSoup(res.text,'lxml')
          My_table = soup.find('table',{'class':'cast_list'})
          if My_table is None:
              print 'Something happened'
              pbz.write(v[0]+"|"+v[1])
              
              continue
          links= My_table.find_all('img')
          

          cast=[]
          for link in links:
              cast.append(link.get('title'))
        
          try:
              for i in range(len(cast)):
                insert_tuple = (v[0],cast[i])
                #print(insert_tuple)
                query = "INSERT INTO  `db` values(%s,%s) "
                cursor.execute(query,insert_tuple)
                
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


