# Thresholding is a method of image segmentation, in general it is used to create binary images. 
# The function cv.threshold is used to apply the thresholding. The first argument is the source image, 
# which should be a grayscale image. The second argument is the threshold value which is used to classify 
# the pixel values. The third argument is the maximum value which is assigned to pixel values exceeding the threshold.
import cv2 as cv
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)
# Simple Threshhold 
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY) # thresh is binarized image whereas threshhold is value we oass fro image in thhis case 150
                                        # shows image whose pixel intensity is greater than 225.
threshold, thresh_inv = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded', thresh)
cv.imshow('Simple Thresholded Inverse', thresh_inv)
# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive thresh', adaptive_thresh)
# 11 is block size and c has a value when we increse we get less y part of images

cv.waitKey(0)