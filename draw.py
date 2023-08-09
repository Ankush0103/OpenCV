import cv2 as cv
import numpy as np
blank = np.zeros((500, 500, 3), dtype='uint8') # uint8 is basically a type of image // blank
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
#blank[200:300, 300:400] = 0, 0, 255      # 255, 0-> Green, 0, 255-> Red
#cv.imshow('Red', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = -1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# 5. Write Text on Image
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)