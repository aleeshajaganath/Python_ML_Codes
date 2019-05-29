# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:19:26 2019

@author: user
"""
import pandas as pd
#pd.read_csv('G:\movie_lense\ml-100k\u.item.txt')

ural1="https://www.imdb.com"
ural2="https://www.imdb.com"
# Open function to open the file "MyFile1.txt" 
# (same directory) in append mode and 
file1 = open("G:\movie_lense\ml-100k\u.txt","r") 
file2= open("testfile1.txt","w") 
#print file1.read() 
print "Output of Readline function is "
#st=file1.readline() 
st=[]
#for link in range(1000):
#    st.append(file1.readline()) 
#    for i in len(str):
#       if st[i]=='T':
#           print st[i]
    
processes = []

with open("G:\movie_lense\ml-100k\u.txt", "r") as f:
    lines = f.readlines()

    print lines

    # Loop through all lines, ignoring header.
    # Add last element to list (i.e. the process name)
    for l in lines[0:]:
        
        
        v= l.split("|")
       
        if v== "unknown" or v==681:
            continue
        
        #print v[1]
       
        p=""
        print v[4]
        p=v[4]
        #file2.write(  v[0]+"\n")
        
        for l in range(len(p)):
            
            if p[l]=="?" :
                
                break
            
         
        q=""  
        l=l+1
        for x in range(l,len(p)):
            print q          
            q=q+p[x]
            
       
        processes.append(q)
                 #file.write( q+"\n")
                 #processes.append( q+"\n")
                 
        print len( p)     
            
#            p.append(v[l])
           
            
file2.close()  
file1.close()       

#print processes
#print "Output of Read(9) function is "
#print file1.read(10) 
#print

# store its reference in the variable file1 
# and "MyFile2.txt" in D:\Text in file2 
#file2 = open(r"D:\Text\MyFile2.txt","w+") 
