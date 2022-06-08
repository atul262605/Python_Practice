# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:53:21 2021

@author: uidj1654
"""
#print("sdfpooosdoosd")
'''sorting the list for length of list elements'''

lst = ["rohan", "amy", "sapna", "muhammad", 
       "aakash", "raunak", "chinmoy"]

def list_sort(list):
   res=sorted(list,key=len)
   return res

#print(list_sort(lst))
#res=lst.sort(key=len)
#print(res)

'''Largest, Smallest, Second Largest, Second Smallest in a List'''

list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]


def find_elements(list1):
      n=len(list1)
      list1.sort()
      print(list1)
      print("smallest element {}".format(list1[0]))
      print("second smallest element {}".format(list1[1]))
      print("largest element {}".format(list1[n-1]))
      print("smallest element {}".format(list1[n-2]))
      
#find_elements(list1)
   
'''Remove duplicate from list'''

from collections import OrderedDict
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]

def remove_duplicate(list1):
   res=list(OrderedDict.fromkeys(list1))
   return res

#print(remove_duplicate(duplicate))

'''Remove all the character other than alphabet'''

input = "$Gee*k;s..fo, r'Ge^eks?"

def Remove_Character(input):
   res=''.join([char for char in input if ord('a')<=ord(char)<=ord('z') or ord('A')<=ord(char)<=ord('Z') ])
   return res

#print(Remove_Character(input))


'''Print anagram in list'''
'''**************************'''
input=['cat', 'dog', 'tac', 'god', 'act'] 

def find_Anagram(list):
    Anagram_Dict={}
    
    for substr in list:
       
       key=''.join(sorted(substr))
       
       if key in Anagram_Dict:
          Anagram_Dict[key].append(substr)
       else:
          Anagram_Dict[key]=[]
          Anagram_Dict[key].append(substr)

    return Anagram_Dict


#print(find_Anagram(input))
# res=[]
# for value in find_Anagram(input).values():
#    res.append(value)

# print(res)

'''#to find index of maximum and minimum element in the array.'''
gfg_list=[8,1,7,10,5]

def find_Max_Min_index(list):
   max=list[0]
   min=list[0]
   max_index=0
   min_index=0
   for i in range(1,len(list)):
      if list[i]<=min:
         min=list[i]
         min_index=i
         
      if list[i]>=max:
         max=list[i]
         max_index=i
   
   print("min :{} \n minimum index :{} \n max :{} \n maximum index :{}".format(min,min_index,max,max_index ))
         
         
#find_Max_Min_index(gfg_list)


'''Concatenated string with uncommon characters in Python'''

str1 = 'aacdb'
str2 = 'gafd'

def Concatenate_string(str1,str2):
   
   common=''.join(set(str1)&set(str2))

   res=''.join([char for char in str1 if char not in common]+[char for char in str2 if char not in common])
   
   return res

#print(Concatenate_string(str1, str2))

'''Remove Columns of Duplicate Elements'''

test_list = [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1],
             [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

def remove_c(list1):
   res=[]
   for sub in list1:
      temp=list(OrderedDict.fromkeys(sub,None))
      res.append(temp)
   return list(res)


#print(remove_c(test_list))



'''Find the number in the list which lies in the range'''

list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80

res=[num for num in list1 if l<=num<=r]

#print(res)
#print(len(res))

'''Check if all the values in a list that are greater than a given value'''

list1 =[10, 20, 30, 40, 50, 2]
val = 5


def Check_values(list1,value):
   Flag=False
   for i in list1:
      if i> value:
         Flag=True
      else:
         Flag=False
         break
   return Flag
      
      
#if Check_values(list1,val):
#   print("All the values are greater then val")
#else:
#   print("False")



'''Python List Comprehension to find pair with given sum from two arrays'''

arr1 = [-1, -2, 4, -6, 5, 7]
arr2 = [6, 3, 4, 0]  
x = 8

def find_pairs(list1,list2,val):
   res= [(i,val-i) for i in list1 if val-i in list2]
   
   print(res)

#find_pairs(arr1,arr2,x)





list1 = [10, 20, 10, 30, 40, 40]

from collections import Counter

count=Counter(list1)

print(count)

for key,value in count.items():
   print(key,value)


'''Maximum sum of elements of list in a list of lists'''


def maximumSum(list1):
   max=0
   
   for sub in list1:
#      if sum(sub)>max:
#         max=sum(sub)
       sum=0
       for i in sub:
          sum=sum+i
       if sum>max:
          max=sum
         
   return max
 

list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
#print (maximumSum(list1))

res=max([sum(sub) for sub in list1])
print('--------------------------------------')
#print(res)

'''Reverse an array upto given position'''


arr = [1, 2, 3, 4, 5, 6]
k = 4

def reverse_arr(arr,k):
   return arr[k-1::-1]+arr[k:]

#print(reverse_arr(arr,k))

'''Count the elements in a list until an element is a Tuple'''

list2= [4, 5, 6, 10, 11,12,(1, 2, 3), 11, 2, 4]

def count_till_tuple(list2):
   count=0
   for i in list2:
      
      if isinstance(i,tuple):
         return count
      else:
         count+=1
    
#print(count_till_tuple(list2))

'''******************************************************'''
'''Program to cyclically rotate an array by one in Python'''
'''******************************************************'''

input = [1, 2, 3, 4, 5]

def cyclicRotate(input):
       
     # slice list in two parts and append
     # last element in front of the sliced list
       
     # [input[-1]] --> converts last element pf array into list
     # to append in front of sliced list
  
     # input[0:-1] --> list of elements except last element
      
    return ([input[-1]] + input[0:-1])

for i in range(2):
   input=cyclicRotate(input)

#print(input)


'''Remove Columns of Duplicate Elements '''
test_list = [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1],
             [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

res=[]
def remove_duplicate_col(test_list):
   for sub in test_list:
      res.append(list(OrderedDict.fromkeys(sub)))
      
   return res


#print(remove_duplicate_col(test_list))

'''******************************************************'''
'''Python program to find Cumulative sum of a list'''
'''******************************************************'''

list1=[10,20,30,40,50]

def cumulative_sum(list1):
   n=len(list1)
   #res=[list1[0]]
   for i in range(0,n-1):
      list1[i+1]=(list1[i]+list1[i+1])
   return list1
      

print("Cumalative sum")
print(cumulative_sum(list1))

'''******************************************************'''
'''Print all sublists of a list in Python'''
'''******************************************************'''
list3=[1,2,3]

def print_subist(list3):
   res=[[]]
   for i in range(len(list3)+1):
      for j in range(i):
         res.append(list3[j:i])
         
   return res


print(print_subist(list3))


'''Reverse an array in groups of given size'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k=3

def reverse_sub(arr,k):
   res=[]
   for i in range(0,len(arr),k):
      res.extend(reversed(arr[i:i+k]))
   return res

#K Numbers only
K_num=arr[k-1::-1]+arr[k:]     
#print(reverse_sub(arr,k))


'''Sort even-placed elements in increasing and odd-placed in decreasing order'''

list5=[0,1,2,3,4,5,6,7]

res=sorted([value for i,value in enumerate(list5) if i%2==0])+sorted([value for i,value in enumerate(list5) if i%2 !=0],reverse=True)

#print(res)



'''find duplicate in test list'''

list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]

def find_duplicate(list1):
   res=[]
   n=len(list1)
   for i in range(0,n):
      k=i+1
      for j in range(k,n):
         if list1[i]==list1[j] and list1[i] not in res:
            res.append(list1[i])
 
         
   return res

#print(find_duplicate(list1))


'''Find minimum in the list '''

list2 = [20, 10, 20, 1, 100]
 
for i in range(len(list2)):
   min=99999
   if min>list2[i]:
      min=list2[i]
   
def find_min(list2):
   min=99999
   for i in range(len(list2)):
      
      if min>list2[i]:
         min=list2[i]
   return min
   

#print(find_min(list2))


'''Find second max in the list'''
list2 = [70, 11, 20, 4, 100]

def find_second_max(list2):
   maximum=max(list2[0],list2[1])
   second_maximum=min(list2[0],list2[1])
   
   for i in range(2,len(list2)):
      if list2[i]>maximum:
         second_maximum=maximum
         maximum=list2[i]
         
      elif list2[i]>second_maximum and maximum !=list2[i]:
         second_maximum=list2[i]

   return second_maximum

#print(find_second_max(list2))



'''Python program to sort a list of tuples by second Item'''

def sort_by_second(list1):
   list1.sort(key=lambda x:x[1])
   return list1

   return(sorted(tup, key = lambda x: x[1]))




tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)] 
#print(sort_by_second(tup))


'''Python program to create a list of tuples from given list having number and its cube in each tuple'''

list1=[1,2,3]

ref=[(i,i**3) for i in list1]

#print(ref)


'''Python program to remove Nth occurrence of the given word'''

list22 = ["geeks", "for", "geeks"]
word = "geeks"
N = 2

def Remove_Nth_Occurance(list22):
   count=0
   index=0
   for i,sub in enumerate(list22):
      if sub==word:
         count+=1
         if count==N:
            index=i
            break
   list22.pop(index)
   return list22



#print(Remove_Nth_Occurance(list22))

'''Intersection of two nested list'''

test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

def intersection_l(list1,list2):
   return [sub for sub in list1 if sub in list2]
   
res_set = set(map(tuple, test_list1)) & set(map(tuple, test_list2))
res_list = list(map(list, res_set))

print(intersection_l(test_list1,test_list2))


# to compute all possible permutations
res = [[i, j, k] for i in list1 
                 for j in list2
                 for k in list3]


 
'''adding string before each list element'''
list22 = [1, 2, 3, 4]
str22='geek'
res=[]
for sub in list22:
   res.append(str22+str(sub))
#print(res)



'''find out given list is subset of another list'''

test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5, 42]



def test_for_sublist(test_list,sub_list):
      flag=0
      for sub in sub_list:
         if sub in test_list:
            flag=True
         else:
            flag=False   

      return flag

flag = 0
if((set(sub_list) & set(test_list))== set(sub_list)):
    flag = 1
     
'''Sort the list according to the other list order'''

test_list = [ ('a', 1), ('b', 2), ('c', 3), ('d', 4)]
 
# initializing sort order
sort_order = ['d', 'c', 'a', 'b']

res=[[sub for i, sub in enumerate(test_list) if test_list[i][0]==j] for j in sort_order]

res = [tuple for x in sort_order for tuple in test_list if tuple[0] == x]

print(res)




'''Remove consecutive duplicates from list'''
test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]

previous=-1

res=[]
for ele in test_list:
   if ele !=previous:
      res.append(ele)
      previous=ele
   else:
      continue
print(res)



'''Merge two sorted list'''

list1 = [25, 18, 9, 41, 26, 31]
list2 = [25, 45, 3, 32, 15, 20]
res=list1+list2

#res.sort()

#res=sorted(res)

#print(res)
 

test_list1 = [[1, 3], [4, 5], [5, 6]]
test_list2 = [[7, 9], [3, 2], [3, 10]]


for i in range(len(test_list1)):
      test_list1[i].extend(test_list2[i])   


#print(test_list1)


obj=(x for x in range(0,11))

print(obj)

for i in range(0,11):
   print(next(obj))


def print_even(test_list) :
    for i in test_list:
        if i % 2 == 0:
            yield i
 
# initializing list
test_list = [1, 4, 5, 6, 7]


print('\n')

gen_obj=(x for x in test_list if x%2==0)

print(gen_obj)

print(next(gen_obj))
print(next(gen_obj))
#print(next(gen_obj))

def nextSquare():
    i = 1
  
    # An Infinite loop to generate squares 
    while True:
        yield i*i                
        i += 1
for num in nextSquare():
   if num>200:
      break
   else:
      print(num)
      
'''
***************************************************************************
Python program to get the indices of each element of one list in another list
'''
test_list = [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3,7]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing get_list 
get_list = [7, 5, 3]


res=[[idx for idx,value in enumerate(test_list)if value==sub] if sub in test_list else [None] for sub in get_list ]

print(res)