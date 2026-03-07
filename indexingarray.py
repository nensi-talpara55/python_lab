#1.positive indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0]) #first element
print(arr[2]) #second element
print(arr[4]) #fifth element

#2. negative indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-1]) #last element
print(arr[-2]) #second last element
print(arr[-5]) #first elelment

#3. modifying elements using index
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

#4. index error
from array import array
arr=array('i',[10,20,30])
print(arr[5])  #error:index out of range