import cv2 as cv
import numpy as np
blank = np.zeros((400, 400), dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)
# AND -> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_AND', bitwise_and)

# OR -> intersecting and non-intersecting regions
bitwise_OR = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_or', bitwise_OR)

# XOR -> non-intersecting regions
bitwise_XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_xor', bitwise_XOR)

# NOT -> 
bitwise_NOT = cv.bitwise_not(rectangle)
cv.imshow('Rectangle_NOT', bitwise_NOT)

cv.waitKey(0)
