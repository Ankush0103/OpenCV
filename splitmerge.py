# OpenCV allows to split an image into multiple color channels 
import cv2 as cv
import numpy as np
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)

b, g, r = cv.split(img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('Blue', blue) # These are depicted as grayscale images that shows distribution of pixel intensities
cv.imshow('Green', green)
cv.imshow('Red', red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
merged = cv.merge([b, g, r]) # Same as original image
cv.imshow('Merged Image', merged)

cv.waitKey(0)