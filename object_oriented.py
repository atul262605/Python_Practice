# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 10:56:26 2022

@author: uidj1654
"""


test_list=[4,2,3,7,5,1,3,4,11,2]

start=test_list[0]
start_index=0
res=[]
for i in range(1,len(test_list)):
   
   if start>test_list[i]:
      continue
       
   res.append(test_list[start_index:i])
       
   start=test_list[i]
   start_index=i
    
res.append(test_list[start_index:])

print("hello")
print(res)

print(bin(2345623))

res=bin(2345623)[2:]
print('0b'+res[::-1])

x=10

 

for i in range(len(bin(x)[2:])):
   bit=x>>i&1
   print(bit)
   
print(bin(x<<1))

test_str="GeeksForGeeksIsBestforGeeks"

 
n=len(test_str)-1
res=[]
while(n!=0):
   res.append(test_str[n])
   n=n-1
   

print(''.join(res))
