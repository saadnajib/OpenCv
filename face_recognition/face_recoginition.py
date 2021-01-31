import cv2 as cv
import numpy as np
import os


face_harcascade = cv.CascadeClassifier('front_face_har.xml')

#creating people labels

people_label = []
DIR = r"images/"

for i in os.listdir(DIR):
    people_label.append(i)

print(people_label)

# reading image and trained yml files

faces_trained = cv.face.LBPHFaceRecognizer_create()
faces_trained.read('faces_trained.yml')
img = cv.imread('C:/Users/admin/Desktop/2.jpg')

# img = cv.resize(img,(800,800),interpolation=cv.INTER_LINEAR)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# detecting faces and getting there cordinates

face_detection = face_harcascade.detectMultiScale(gray,1.1,5)

# croping the face with cordinates and creating a rectangle

for (x,y,w,h) in face_detection:
    face_roi = gray[y:y+h,x:x+w]
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255) , 2)

# making predictions on the croped image

lable, confidence = faces_trained.predict(face_roi) 

# putting predicted label name on the bounding box

cv.putText(img,people_label[lable],(x-20,y-10),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

print(f'index: {lable} and confidence: {confidence}')
cv.imshow('face1',img)
cv.imshow('face2',face_roi)
cv.waitKey(0)