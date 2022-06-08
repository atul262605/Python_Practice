# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 19:33:09 2021

@author: uidj1654
"""
sample_str = "This is a sample string"
char_to_replace = {1: 'X',
                   3: 'Y',
                   5: 'Z'}
#print("hello world")

#for key,value in char_to_replace.items():
#   sample_str=sample_str[:key]+value+sample_str[key+1:]

K=2
repl='K'
res=[]
n=len(sample_str)
for i in range(0,n+1,2*K):
   #sample_str=sample_str[:i]+repl+sample_str[i+1:]
   res.append(sample_str[i])


print(sample_str)
print(res)

def class_decorator(func):
   
   def class_method_wraper(self,arg):
      arg="mr "+arg
      func(self,arg)
      
   return class_method_wraper


class my_class:
   def __init__(self,name):
      self.name=name
   
   @class_decorator   
   def method_to_decorate(self,name):
      print("my name is {}".format(name) )
      
def test_func():
   print("hello world")

if __name__=="__main__":      
   
   obj=my_class("atul")

   obj.method_to_decorate("Atul Sharma")

   print("if execute directly")

#decorator which accept paramenters


def decorator_make(decorator_arg1,decorator_arg2):
   
   def function_decorator(func_to_decorate):
      
      def wraper_function(*arg,**kwarg):
         
         print("inside wraper function")
         
         print("Received 2 decorator arguments {}, {}".format(decorator_arg1,decorator_arg2))
         func_to_decorate(*arg,**kwarg)
         
         print("at the end of funcion wraper")
         
      return wraper_function
   
   return function_decorator

@decorator_make(12,23)
def function_1(*arg,**kwarg):
   print(*arg,end='\n')
   print(**kwarg)
   
   
function_1(sample_str,char_to_replace)




# decorator to identify how many times function is called

def decorator_to_count_func_call(func):
   
   def wraper(*args,**kwargs):
    
      func(*args,**kwargs)
      print("func name and counter which is being decorate {},{},{}".format(func.__name__,args,kwargs))
         
      print("----------------------------------")
   return wraper

@decorator_to_count_func_call
def func(*args,**kwargs):
   print("hello world")
dict11={'param3': 9, 'param1': 5, 'param2': 8} 
func()
func(1,2,key_4=5,**dict11)


#using __call__ making object callable

class test(object):
   def __inti__(self):
      print("Object is instentiated")
      
   def __call__(self):
      print("Inside call function")
      
      
obj=test()

obj()

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

K=3

res=[]
temp=dict()
count=0
for key,value in test_dict.items():
   
   temp[key]=test_dict[key]
   count+=1
   
   if count%K==0:
      res.append(temp)
      temp={}
 

print(res)


test_list = [3, 4, 7, 5, 6, 7, 3, 4, 6, 9]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing K 
K = 5
  
# initializing repl_chr 
repl_chr = "NA"

res=[]
for sub in test_list:
   if sub>K:
      res.append(repl_chr)
   else:
      res.append(sub)
      
print(res)


res1=[repl_chr if sub>K else sub for sub in test_list ]





arr=[1,3,5,4,2]

arr.sort(reverse=True)

print("{}".format(sum(arr[1:])))

print(arr)