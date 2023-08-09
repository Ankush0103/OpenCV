import cv2 as cv
import numpy as np

img = cv.imread('messifoot.jpg')
cv.imshow('Messi', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotations
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) # -45 -> C.W, 45 -> A.C.W
cv.imshow('Rotated', rotated) 
# 2 times rotation
rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # Enlarging the image
cv.imshow('Resized', resized)

# Flipping
# 0->Flipping vertically i.e. over x-axis, 1->Flipping image horizontally i.e. over y-axis
# -1->Flipping both vertically and horizontally
flip = cv.flip(img, -1) 
cv.imshow('Flip', flip)
cv.waitKey(0)