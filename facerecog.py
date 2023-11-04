import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # -ve or 0 to Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
         gray,     
         scaleFactor=1.2,
         minNeighbors=5,     
         minSize=(20, 20)
    )
    # cv2.imshow('gray', gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]  
    cv2.imshow('video', frame)
    if cv2.waitKey(30) & 0xff==ord('s'):
         break
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
 
leo_image = face_recognition.load_image_file("leo.jpeg")
leo_encoding = face_recognition.face_encodings(leo_image)[0]
 
lady_image = face_recognition.load_image_file("lady.jpg")
lady_encoding = face_recognition.face_encodings(lady_image)[0]
 
messiwc_image = face_recognition.load_image_file("messi-wc.jpg")
messiwc_encoding = face_recognition.face_encodings(messiwc_image)[0]
 
# tesla_image = face_recognition.load_image_file("photos/tesla.jpg")
# tesla_encoding = face_recognition.face_encodings(tesla_image)[0]
 
known_face_encoding = [
leo_encoding,
lady_encoding,
messiwc_encoding
# tesla_encoding
]
 
known_faces_names = [
"Leo Messi",
"Random Lady",
"Messi WC",
#"tesla"
]
 
students = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
s=True
 
 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
 
 
 
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)
 
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # -ve or 0 to Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
         gray,     
         scaleFactor=1.2,
         minNeighbors=5,     
         minSize=(20, 20)
    )
    # cv2.imshow('gray', gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]  
    cv2.imshow('video', frame)
    if cv2.waitKey(30) & 0xff==ord('s'):
         break
    # _,frame = cap.read()
    # small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    # rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2
 
                cv2.putText(frame,name+' Present', 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
 
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
 
cap.release()
cv2.destroyAllWindows()
f.close()