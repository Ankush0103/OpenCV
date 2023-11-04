import cv2 as cv
#import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ankush', 'Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Leo Messi', 'Madonna']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
# Do Loop

faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# cv.imshow('Person', frame)
img= cv.imread(r"D:\OpenCV\Faces\val\ankush\Ankush_Passport_Photograph.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)
# cap = cv.VideoCapture(0)
# cap.set(3,640) # set Width
# cap.set(4,480) # set Height
# while True:
#     ret, frame = cap.read()
#     frame = cv.flip(frame, 1) # -ve or 0 to Flip camera vertically
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(
#          gray,     
#          scaleFactor=1.2,
#          minNeighbors=5,     
#          minSize=(20, 20)
#     )
#     # cv2.imshow('gray', gray)
#     for (x,y,w,h) in faces:
#         cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]  
#     cv.imshow('videolive', frame)
#     if cv.waitKey(30) & 0xff==ord('s'):
#          break
# cap.release()
# img = cv.imread(frame)

# Detect face in image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected image', img)
cv.waitKey(0)