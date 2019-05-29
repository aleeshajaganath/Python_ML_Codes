# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:30:40 2019

@author: user
"""

"""_________________________________converting to id______________________________"""
""" fetching the movie url from the site  and sve in url_id_1.txt file"""
from HTMLParser import HTMLParseError
import requests

import bs4
file1 = open("url_id_2.txt","w") 
pbz = open("url_id_pbz.txt","w") 
p=[]
try:
   with open("url.txt","r")  as f:
    lines = f.readlines()
   # print "\n",lines
    st='https://www.imdb.com'
    
    for l in lines[0:118]:
          v= l.split("|")
          print (v[0])
          res= requests.get(v[2])
          soup= bs4.BeautifulSoup(res.text,'lxml')
          My_table = soup.find('table',{'class':'findList'})
          if My_table is None:
              print 'Something happened'
              pbz.write(v[0]+"|"+v[1])
              
              continue
          #print  My_table
          links= My_table.find_all('a')
          
                
          cast=[]
          
          na=[]
          
          for link in links:
          
              cast.append(link.get('href'))
               
              
              
              
              na.append(link.text)

            
          file1.write(v[0]+"|"+st+cast[0]+"\n")
except HTMLParseError:
    pass
    msg = ("Unable to create file on disk.")
    file1.close()
    
file1.close()
pbz.close()
    #return
                    
#    res= requests.get('https://www.imdb.com/find?q=Schrei%20aus%20Stein%20(1991)&s=tt&ttype=ft&ref_=fn_ft')
#
#soup= bs4.BeautifulSoup(res.text,'lxml')
##print(soup.get_text())
#body =soup.body
#div=soup.div
#
##for div in  body.find_all('div'):
##    print(div.id)
##result_text
##
#My_table = soup.find('table',{'class':'findList'})
#links= My_table.find_all('a')
#
#cast=[]
#na=[]
#for link in links:
#  cast.append(link.get('href'))
#  na.append(link.text)
