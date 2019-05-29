# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:27:42 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:30:40 2019

@author: user
"""
''' 
https://www.imdb.com/find?q=Schrei%20aus%20Stein%20(1991)&s=tt&ttype=ft&ref_=fn_ft'''
'https://www.imdb.com/find?q=Schrei%20aus%20Stein%20(1991)&s=tt&ttype=ft&ref_=fn_ft'
'https://www.imdb.com/find?q=Usual%20Suspects  &s=tt&ttype=ft&ref_=fn_ft'
'https://www.imdb.com/find?q=GoldenEye    &s=tt&ttype=ft&ref_=fn_ft'
'Dead%20Man%20Walking%20'

'https://www.imdb.com/find?q=Dead%20Man%20Walking%20(1995)&s=tt&ttype=ft&ref_=fn_ft'
import requests

import bs4
res= requests.get('https://www.imdb.com/find?q=Se7en%20(1995)&s=tt&ttype=ft&ref_=fn_ft')

soup= bs4.BeautifulSoup(res.text,'lxml')
#print(soup.get_text())
body =soup.body
div=soup.div

#for div in  body.find_all('div'):
#    print(div.id)
#result_text
#findList
My_table = soup.find('table',{'class':'findList'})
links= My_table.find_all('a')

cast=[]
na=[]
for link in links:
  cast.append(link.get('href'))
  cast.append(link.text)
