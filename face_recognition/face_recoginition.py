import cv2 as cv
import numpy as np
import os


face_harcascade = cv.CascadeClassifier('front_face_har.xml')

people_label = []
DIR = r"images/"

for i in os.listdir(DIR):
    people_label.append(i)

print(people_label)

faces_trained = cv.face.LBPHFaceRecognizer_create()
faces_trained.read('faces_trained.yml')

img = cv.imread('C:/Users/admin/Desktop/1.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_detection = face_harcascade.detectMultiScale(gray,1.1,3)

for (x,y,w,h) in face_detection:
    face_roi = gray[y:y+h,x:x+w]
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255) , 2)

lable, confidence = faces_trained.predict(face_roi) 

cv.putText(img,people_label[lable],(x-20,y-10),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
print(f'index: {lable} and confidence: {confidence}')



cv.imshow('face1',img)
cv.imshow('face2',face_roi)

cv.waitKey(0)