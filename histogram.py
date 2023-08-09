# A histogram is a very important tool in Image processing. It is a graphical representation of 
# the distribution of data. An image histogram gives a graphical representation of the distribution 
# of pixel intensities in a digital image.
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)
# blank = np.zeros(img.shape[:2], dtype = 'uint8')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)
# # Grayscale Histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()
# Colour Histogram
colors = {'b', 'g', 'r'}
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])   
plt.show() 
cv.waitKey(0)