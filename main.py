# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:21:54 2022

@author: hamidat
"""
from PIL import Image
import numpy as np


filin = open("last_image.txt", "r")
rows=int(filin.__iter__().__next__())

cols=int(filin.__iter__().__next__())



#Create a 2 dimensional list using rows nd cols
#write here
matrix = 




#Fill in the double loop in order to fill the matrix
for y in range(rows):
    #write here
  
     
     for x in range(cols):
         #write here
         

#TEST if it is ok    -->just check
print(arr[2][1])    

#Close the file 'last_image

#write here


#Find the minimum of the matrix below, store it inside the variable min

#write here


min=0
#Find the maximum of the matrix below, store it inside the variable max

#write here

max=0

#TEST check the max and min values -->just check
print("max is: ",max," min is: ", min)


#compute the equation parameters (see https://www.google.com/search?q=Calculates+the+linear+equation+given+two+points)
a=float( ( 255.0   / ( #write here ))) ;
b = #write here;


#Create a B&W image with the good size and load it

#write here



#Fill in the image pixel by pixel
for y in range(len(arr)):
    for x in range(len(arr[0])):
        #write here

new_image.save('foo.png', 'png')
