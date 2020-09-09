#!/usr/bin/env python
# coding: utf-8

# In[27]:


# generate random floating point values
from random import random
import matplotlib.pyplot as plt
import math
import numpy as np
import random 

print("Pi Calculator launched! Welcome")
def pigenerator():

    def scale(value):
        value = 0 + (value * (1)) #range number from 0-1
        return(value)
    global samplesize #set as 'global' in a seperate line
    samplesize = random.randint(100, 1000000)
    #samplesize=int(input("Enter a sample size: "))    
    #prompt user to enter an integral input
    
    #define x and y values list
    listx=[]
    listy=[]

    # generate random numbers between 0-1
    for i in range(samplesize): #generate random nos. for x-values
        value = random.random()
        listx.append(scale(value))
    #print("x-coordinates: ")
    #print(listx)

    # generate random numbers between 0-1
    for i in range(samplesize): #generate random nos. for y-values
        value = random.random()
        listy.append(scale(value))
    #print("y-coordinates: ")
    #print(listy)

    #plot
    #plt.plot(listx, listy)

    #find the distance from origin
    list_d=[]
    for i in range(samplesize):
        a=listx[i]
        b=listy[i]
        c=math.sqrt(a**2+b**2)
        list_d.append(c)
    #print("Distance: ")
    #print(list_d)

#test my sqrt functions
#a=1.2
#b=3
#c=math.sqrt(a**2+b**2)
#print("Test: ")
#print(c)

#screen out random nos. outranged distance=1
    list_useful=[]
    setvalue=1
    for i in list_d:
        if i < setvalue: #list comparasion not available between list and float => shall obtain values through i
            list_useful.append(i)
#print("Distance less than 1: ")
#print(list_useful)
    print("Useful points: ", len(list_useful))
    print("Total points: ", len(list_d))

    Ratio=len(list_useful)/len(list_d)
    print("Ratio: ", Ratio)

#find pi
    pi=Ratio*4
    print("Pi: ", pi)
    return pi #call out pi as output, when the function is used


# In[33]:


list_size=[]
list_pi=[]

print("Enter the no. of trial: ")
selectedrange=int(input())

for i in range(selectedrange):
    pi=pigenerator()
    list_size.append(samplesize) #with 'samplesize' as global
    list_pi.append(pi)

#print("The sample size is: ", list_size)
#print("The sample pi is: ", list_pi)


# In[34]:


print(list_size)
plot1=plt.plot(list_size, list_pi, 'r.') #add 'r.' as the last parameter to plot points instead of lines
plt.grid(True) #show grid lines
plt.hlines(np.pi, 100, 1000000) #plt.hlines(constant, min, max) <- to plot a horizontal line
plt.ylabel('Numerical value of pi')
plt.xlabel('Sample size')


# print(list_size)
# plot1=plt.plot(list_size, list_pi)
# plt.ylabel('Numerical value of pi')
# plt.xlabel('Sample size')

# In[ ]:


#find e correspondingly

