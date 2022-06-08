# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:26:07 2021

@author: uidj1654
"""

print('exception handling')


try:
   f=open('tes33t.txt','r')
   var=10
   if _var==10:
      raise Exception
except NameError:
   print("Assignment value is not corrrect")
     
except FileNotFoundError:
   print('Not able to find the file in directory')
   
except Exception:
   print("hello world")
else:
   print(f.read())
   f.close()
finally:
   print('----------------------')
   
   
class A(object):
   def __init__(self):
      print("This is A class constructor")
      
   def A_method(self):
      print("This is class A method")
      
class B(A):
   def __init__(self):
      print("This is class B constructor")
      super().__init__()
   def A_method(self):
      print("This is class B method")

class C(B):
   def __init__(self):
      print("This is class c constructor")
   
   def A_method(self):
      print("This is class C method")
      super(B,self).A_method()
      

b=B()
c=C()
c.A_method()