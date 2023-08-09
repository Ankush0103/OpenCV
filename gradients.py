# Laplacian Operator is also a derivative operator 
# which is used to find edges in an image. It is a second order derivative mask.
import cv2 as cv
import numpy as np
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# Laplacion
lap = cv.Laplacian(gray, cv.CV_64F)
lap= np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
# Sobel -> computes gradient in two direction x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('Combined Sobel', combined_sobel)
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)