import cv2 as cv
import numpy as np
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)

# Converting to GrayScale, since BGR images should be converted to grayscale so that we see the intensity
# distrubution of pixels
gray = cv. cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Converting to blur to reduce bad lighting in image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge cascades to find number of edges in image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) 
# resizes ignoring the aspect ratio, interpolation = cv.INTER_AREA is useful if you are shrinking image
#                                   # interpolation = cv.INTER_CUBIC is useful if you are shrinking image 
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
