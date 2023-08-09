import cv2 as cv
img = cv.imread('messifoot.jpg')
cv.imshow('messifoot', img)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Rescaled Image', resized_image)
# Reading Videos
'''capture = cv.VideoCapture('My Video.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame_resized)
    # To stop
    if cv.waitKey(20) & 0xFF==ord('s'): # if letter s is pressed break out of the loop. 
        break
capture.release()
cv.destroyAllWindows()'''
cv.waitKey(0)
    