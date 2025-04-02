from PIL import Image
import numpy as np


filin = open("input.txt", "r")


rows = int(filin.__iter__().__next__())
cols = int(filin.__iter__().__next__())


# create a 2 dimensional list using rows nd cols
matrix = np.zeros((rows, cols))


# fill in the double loop in order to fill the matrix
for y in range(rows):
    row = filin.__iter__().__next__()
    row = row.rstrip(" ").lstrip(" ").split(" ")

    for x in range(cols):
        matrix[y, x] = int(row[x])
         

# close the file 'input' file
filin.close()


# find the minimum and the maximum of the matrix below, store it inside the variable min
min, max = matrix[0, 0], matrix[0, 0]
for y in range(rows):
    
    for x in range(cols):
        
        value = matrix[y, x]
        
        if value < min:
            min = value
        if value > max:
            max = value
        

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

# save output
new_image.save('output.png', 'PNG')