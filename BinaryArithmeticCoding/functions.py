import numpy as np
def squareImage(imgArr, imageHeight, imageWidth, vectorHeight, vectorWidth):
    if (imageHeight) % vectorHeight != 0:
        newimageHeight = ((imageHeight//vectorHeight) + 1) * vectorHeight
    if imageWidth % vectorWidth != 0:
        newimageWidth = ((imageWidth//vectorWidth) + 1) * vectorWidth
    col = 0
    row = 0
    i = 0
    j = 0
    arr = [9][5]
    for i in range(5):
        col = i
        for j in range(9):
            row = j
            if (i+1) > imageHeight or (j+1) > imageWidth:
                arr[i][j] = 0
            else:
                arr[i][j] = imgArr[col][row]
    return arr