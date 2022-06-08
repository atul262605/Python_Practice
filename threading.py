# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:00:49 2022

@author: uidj1654
"""

print("Bit manipulation")

n=0b1000

print(bin(n))

hex_1=0xFF

#print(bin(hex_1<<4))

i=31
mask=(n<<(i+1))
print(bin(mask))

print(bin(1<<(i+1)))

print(bin(1<<10))

import datetime

print(str(datetime.datetime.now()))
print(repr(datetime.datetime.now()))

n=32
print(bin(n))
print(bin(1<<5))

n=n|(1<<4)

print(bin(n))

x=15
y=9

print(bin(x))
print(bin(y))

print(bin(x or y))

print("hello")
count=0
while x:
   count+=x&1
   x=x>>1
print(count)




test_list = [4, 3, 8, 2, 6, 7, 4, 3, 2, 4, 5]

K=4
res=[]
for idx in range(0,len(test_list),K):
   print(test_list[idx:idx+K])
   
      
      
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

y=sorted(x.items(),key=lambda value:value[0])

print(y)   

#x = [
# ['4', '21', '1', '14', '2008-10-24 15:42:58'], 
# ['3', '22', '4', '2somename', '2008-10-24 15:22:03'], 
# ['5', '21', '3', '19', '2008-10-24 15:45:45'], 
# ['6', '21', '1', '1somename', '2008-10-24 15:45:49'], 
# ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
#]





#from operator import itemgetter
#
#x.sort(key=lambda x:(x[0],x[1]))
#
#
#print(x)

def sort_dict(item: dict):
    """
    Sort nested dict
    Example:
         Input: {'a': 1, 'c': 3, 'b': {'b2': 2, 'b1': 1}}
         Output: {'a': 1, 'b': {'b1': 1, 'b2': 2}, 'c': 3}
    """
    return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}

input_dict={'a': 1, 'c': 3, 'b': {'b2': 2, 'b1': 1}}

print(sort_dict(input_dict))




test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
             'Akshat' : {'roll' : 54, 'marks' : 12}, 
             'Akash' : { 'roll' : 12, 'marks' : 15}}
  


print(sort_dict(test_dict))

res = sorted(test_dict.items(), key = lambda x: x[1]['marks'])


print(dict(res))









