# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:30:40 2019

@author: user
"""

import requests

import bs4
res= requests.get('https://www.imdb.com/find?ref_=nv_sr_fn&q=Toy+Story+&s=tt')

soup= bs4.BeautifulSoup(res.text,'lxml')
#print(soup.get_text())
body =soup.body
div=soup.div

#for div in  body.find_all('div'):
#    print(div.id)

My_table = soup.find('table',{'class':'findList'})
links= My_table.find_all('a')

cast=[]
na=[]
for link in links:
  cast.append(link.get('href'))
  na.append(link.text)
