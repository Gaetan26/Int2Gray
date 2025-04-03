

import numpy as np
from PIL import Image


#
#
def extractImageSize(fileinput):
    rows = int(fileinput.__iter__().__next__())
    cols = int(fileinput.__iter__().__next__())
    
    return (rows, cols)


#
#
def createMatrix(rows, cols):
    return np.zeros((rows, cols))


#
#
def fillMatrix(fileinput, matrix):
    rows, cols = matrix.shape
    
    for y in range(rows):
        row = fileinput.__iter__().__next__()
        row = row.rstrip(" ").lstrip(" ").split(" ")
        
        for x in range(cols):
            matrix[y, x] = int(row[x])
    
    return True


#
#
def findMinMaxValues(matrix):
    rows, cols = matrix.shape
    minval, maxval = matrix[0, 0], matrix[0, 0]
    
    for y in range(rows):
        for x in range(cols):
            value = matrix[y, x]
            minval = value if value < minval else minval 
            maxval = value if value > maxval else maxval 
    
    return minval, maxval


#
#
def findParamatersOfLinearEquation(minval, maxval):
    m = 255 / (maxval - minval)
    b = -minval * m

    return m, b


#
#
def createGrayscaleImage(rows, cols):
    image = Image.new('L', (cols, rows))
    pixels = image.load()

    return image, pixels


#
#
def matchMatrixValuesWithPixels(matrix, pixels, m, b):
    rows, cols = matrix.shape
    for y in range(rows):
        for x in range(cols):
            value = round(m * matrix[y, x] + b)
            pixels[x, y] = min(255, max(0, value))
    
    return True


#
#
def saveImage(image, name, format_):
    image.save(f"{name}.{format_}", format_)
    return True


#
#
def process(fileinput, output, format_):
    
    try:
        # ouvrir le fichier avec les entrees
        fileinput = open(fileinput, "r")
        
        # extraires la taille de l'image + creer la matrice
        rows, cols = extractImageSize(fileinput)
        matrix = createMatrix(rows=rows, cols=cols)
        
        # remplir la matrice avec les valeurs d'entrees
        fillMatrix(fileinput=fileinput, matrix=matrix)
        
        # fermer le fichier des entrees
        fileinput.close()

        # trouver la valeur MINIMAL & MAXIMAL
        minval, maxval = findMinMaxValues(matrix)

        # trouver les parametres de l'equation lineaire
        m, b = findParamatersOfLinearEquation(minval=minval, maxval=maxval)

        # creer une image en GRAYSCALE
        image, pixels = createGrayscaleImage(rows=rows, cols=cols)
        matchMatrixValuesWithPixels(matrix=matrix, pixels=pixels, m=m, b=b)
        
        # sauvegarder l'image
        saveImage(image=image, name=output, format_=format_)

        return True
    
    except:
        return None
