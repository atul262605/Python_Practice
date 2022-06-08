# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:42:19 2021

@author: uidj1654
"""

print("This is the file handling")

#f=open('test.txt','r')
#
#for line in f:
#   print(line)
#print(f)
#print(f.mode)
#f.close()

with open ('test.txt','r') as fd:
   with open('test2.txt','w') as fw:
      lines=fd.read()
      fw.write(lines)
   
#print(lines)
   
 