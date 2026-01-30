#sorted search with conditions
from random import random

values =[random() for i in range(20)]
x= random()
values.sort()# I'm sorting the values of the original list.

sorted_list=[element for element , val in enumerate(values) if val >= x]# this is my new sorted list
print("The sorted list is: ", sorted_list)# I'm printing out the sorted list as required
print("The value of x: ",x)#Printing out the value of x as required

if sorted_list:
    print("The first matching index: ",sorted_list[0])#printing the value of the first matching index if it exists
else:
    print("There is no first matching index.")




