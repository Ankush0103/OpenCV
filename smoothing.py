import cv2 as cv
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)
# Averaging finads average of suurounding pixel in blur 
average = cv.blur(img, (3, 3)) # As we increase (x, y) blur increases
cv.imshow('Average Blur', average)
# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)
# Median Blur finds median of surrounding pixel, it is more effective in reducing noise of an image
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral', bilateral) # For large values looks like smudged version of this image
cv.waitKey(0)