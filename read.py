# OpenCv stands for Open Source Computer Vision Library.
# OpenCV is an open-source library for the computer vision. 
# It provides the facility to the machine to recognize the faces or objects
import cv2 as cv
#img = cv.imread('dragon.png')
#cv.imshow('dragon.png', img) # Displays image in a new window
# Reading Videos
capture = cv.VideoCapture('My Video.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    # To stop
    if cv.waitKey(20) & 0xFF==ord('s'): # if letter s is pressed break out of the loop. 
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
