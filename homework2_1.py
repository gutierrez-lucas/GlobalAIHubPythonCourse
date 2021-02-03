"""
SECOND HOMEWORK

1) Create a list and swap the second half of the list with the first half of the list and print the list on screen

"""
import random

print("A list of random size filled with random numbers will be created..")

list_random = []
list_size = random.randint(10,15)

aux_value = 0 #not needed to be initialized. just out of habit

#if not even there is no 'half'

#if list_size % 2!=0: 
#    list_size += 1
    
list_size += 1 if list_size%2 != 0 else list_size

print("The list will be filled with %d characters" %(list_size))

for i in range(0, list_size):
    list_random.append(random.randint(1,100))
    
print(list_random)
half = (int)(list_size/2) 

print("Half point: ", half)

for i in range(0, half):  
    aux_value = list_random[i]
    list_random[i] = list_random[half + i]   
    list_random[half + i] = aux_value

print(list_random)