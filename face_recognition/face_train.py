import cv2 as cv
import numpy as np
import os

labels = []
features = []

face_harcascade = cv.CascadeClassifier('front_face_har.xml')

#creating people labels

people_label = []
DIR = r"images/"

for i in os.listdir(DIR):
    people_label.append(i)

print(people_label)

# creating train function

def creat_train():
    
    for people in people_label:    
        path = os.path.join(DIR,people)
        label = (people_label.index(people))
        
        for img in os.listdir(path):

            images = os.path.join(path,img)
            pictures = cv.imread(images)
            gray = cv.cvtColor(pictures,cv.COLOR_BGR2GRAY)

            face_cordinates = face_harcascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
            for (x,y,w,h) in face_cordinates:    
                faces = gray[y:y+h,x:x+w]
                
                features.append(faces)
                labels.append(label)



    print(len(features))
    print(len(labels))

            
creat_train()
print("training Done1")

features = np.array(features,dtype=object)
labels = np.array(labels)

# training face features and labels 

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

# Saving trained model, features and labels

face_recognizer.save('faces_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)

print("saving Done")
