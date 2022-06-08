matrix = [[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]

print(matrix)
res=[[sub[i] for sub in matrix] for i in range(len(matrix[1]))]

print(res)

input = [12, 10, 9, 45, 2, 10, 10, 45]


from collections import Counter

input1 = [12, 10, 9, 45, 2, 10, 10, 45]

count=Counter(input1)

res=[]
for key,value in count.items():
   if value==1:
      res.append(key)
      
print(res)


res=[]
for value in input1:
   count=0
   for i in range(len(input1)):
      if value==input1[i]:
         count+=1
   if count==1:     
      res.append(value)
      
print(res)

from collections import OrderedDict

d1={'a':1,'b':3,'c':5,'d':12}
d2={'a':11,'b':13,'c':15}

k1=list(OrderedDict.fromkeys(d1).keys())
k2=list(OrderedDict.fromkeys(d2).keys())

print(k1)
print(k2)

test=k1+k2
keys=[]

for key in test:
   if key not in keys:
      keys.append(key)
      

#k1=[k for k in d1.keys()]
#k2=[k for k in d2.keys()]

#keys=set(k1+k2)

res={k:[d1.get(k,0),d2.get(k,0)] for k in keys}

print(res)


test={'a': [1, 11], 'b': [3, 13], 'c': [5, 15], 'd': [12, 0]}

from collections import defaultdict
res=dict()
for key,value in test.items():
      temp=[]
      if isinstance(value,list):
         res[key]=[]
         for v in value:
            if v:
               res[key].append(v)
   
print(res)   
   
   
   
   
str1="hElloa"

print(''.join(sorted(str1)))



byte_list=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

bit_no_to_set=131

total_num_of_bits=len(byte_list)*16
                     
byte_position=131//16

bit_position=131%16-1

byte_list[byte_position]|=1<<bit_position
         
print(byte_list)