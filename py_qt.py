print("hello world")

def test_func():
    print("hello world")

test_func()



test_str="GeeksForGeeks"

 
      
n=len(test_str)-1
res=[]
while(n>=0):
   res.append(test_str[n])
   n-=1
   

print(''.join(res))
 

test_list=[0,1,1,0,1]

start=test_list[0]
count=0
for i in range(1,len(test_list)):
   
   if start !=test_list[i]:
      count+=1
   start=test_list[i]

print(count)

test_list2=[-1,-1,-1,-1,-1]

prev=test_list2[0]
counter=0
for i in range(1,len(test_list2)):
   next_ele=test_list2[i]
   
   if next_ele == - prev:
      counter+=1
   prev=test_list2[i]
   
print(counter)

























