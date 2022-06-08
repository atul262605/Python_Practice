# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:08:24 2019

@author: uidj1654
"""

print("hello world")
 
    

test_list3=[-1,2,3,-5,-7,8,9,-10]

a =[i for i in test_list3 if i<0] 
b=[i for i in test_list3 if i>=0] 
 
print(a)
print(b)


x=list(filter(lambda x:x<0,test_list3))

y=list(filter(lambda x:x>=0,test_list3))

print(x)
print(y)