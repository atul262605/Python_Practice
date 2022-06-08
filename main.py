# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:56:51 2021

@author: uidj1654
"""
from temp import test_func

print("hello world")

test_func()


#finding duplicate in string

str1="Geeks for Geeks"

dict1={}
for st in str1.split():
   if st in dict1.keys():
      dict1[st]+=1
   else:
      dict1[st]=1
           
for key in dict1:
   if dict1[key]>1:
      print(key,end="")
      
      
for ch in str1:
   print(ch)
   
   
str2="MalyalaM"

n=len(str2)
for i in range(0,int(n/2)):
   if str2[i]==str2[n-1-i]:
      print("string is plindrome")
      break
   
dict2={'a':1,'b':1,'c':3,'d':4,'e':1}

rev_Dict={}

for key, value in dict2.items():
   if value not in rev_Dict:
      rev_Dict[value]=[key]
            
   else:
      rev_Dict[value].append(key)
              
print(rev_Dict)