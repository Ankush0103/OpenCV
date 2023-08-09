# Countours are basically the boundaries of objects, line or curve that joins the continous points along
# the boundary of an object. But they are not same as edges. Contours are useful tools when we get into 
# shape analysis, object detection and recognition.

import cv2 as cv
import numpy as np
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
#We need to grab the edges through the canny edge detector
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
# Contours is a list
print(f'{len(contours)} contours found!')
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)