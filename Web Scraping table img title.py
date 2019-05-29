# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 00:15:14 2019

@author: user
"""
import requests

import bs4
file1 = open("cast.txt","w") 
with open("url_id_1.txt","r")  as f:
    lines = f.readlines()
   # print "\n",lines
    st='https://www.imdb.com'
    
    for l in lines[0:1]:
          v= l.split("|")
          print (v[1])
          res= requests.get(v[1])

          soup= bs4.BeautifulSoup(res.text,'lxml')
          My_table = soup.find('table',{'class':'cast_list'})
          links= My_table.find_all('img')

          cast=[]
          for link in links:
              cast.append(link.get('title'))
        
          for i in range(len(cast)):
              file1.write(v[0]+"|"+cast[i]+"\n") 
              print(v[0]+"|"+cast[i]+"\n") 
file1.close()

#print(soup.get_text())
#body =soup.body
#div=soup.div

#for div in  body.find_all('div'):
#    print(div.id)


