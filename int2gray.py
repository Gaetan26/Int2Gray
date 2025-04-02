

import numpy as np
from PIL import Image
from time import strftime


def extractImageSize(fileinput):
    rows = int(fileinput.__iter__().__next__())
    cols = int(fileinput.__iter__().__next__())
    
    return (rows, cols)


def createMatrix(rows, cols):
    return np.zeros((rows, cols))


def fillMatrix(fileinput, matrix):
    rows, cols = matrix.shape
    
    for y in range(rows):
        row = fileinput.__iter__().__next__()
        row = row.rstip(" ").lstrip(" ").split(" ")
        
        for x in range(cols):
            matrix[y, x] = int( row[x] )
    
    return True


def findMinMaxValues(matrix):
    rows, cols = matrix.shape
    minval, maxval = matrix[0, 0], matrix[0, 0]
    
    for y in range(rows):
        
        for x in range(cols):
            value = matrix[y, x]
            minval = value if minval < value else minval 
            maxval = value if maxval > value else minval 
    
    return minval, maxval


def findParamatersOfLinearEquation(minval, maxval):
    m = 255 / (maxval - minval)
    b = -minval * m

    return m, b


def createGrayscaleImage(rows, cols):
    image = Image.new('L', (cols, rows))
    pixels = image.load()

    return image, pixels


def matchMatrixValuesWithPixels(matrix, pixels, m, b):
    rows, cols = matrix.shape
    for y in range(rows):
        for x in range(cols):
            value = round(m * matrix[y, x] + b)
            pixels[x, y] = min(255, max(0, value))
    
    return True


def saveImage(image):
    image.save(strftime("%c")+".png", "PNG")
    return True