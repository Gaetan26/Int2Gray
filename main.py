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
min_, max_ = matrix[0, 0], matrix[0, 0]
for y in range(rows):
    
    for x in range(cols):
        
        value = matrix[y, x]
        
        if value < min_:
            min_ = value
        if value > max_:
            max_ = value
        
# compute the equation parameters
a = float(255.0 / (max_-min_))
b = -min_ * a

# create a B&W image with the good size and load it
new_image = Image.new('L', (cols, rows))
image_pixels = new_image.load()

# fill in the image pixel by pixel
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        value = round( a * matrix[y, x] + b )
        image_pixels[x, y] = min(255, max(0, value))

# save output
new_image.save('output.png', 'PNG')