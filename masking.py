# Masking is a common technique to extract the Region of Interest (ROI). 
# OpenCV Image Masking is a powerful for manipulating images. 
# It allows you to apply effects to a single image and create an entirely new look.
import cv2 as cv
import numpy as np
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
weird = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird', weird)
# mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)
masked = cv.bitwise_and(img, img, mask = weird)
cv.imshow('Masked Image', masked)
cv.waitKey(0)