import cv2 as cv

img = cv.imread('p/p7.jpg')
cv.imshow('people',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Face detection through Harcascade

face_harcascade = cv.CascadeClassifier('front_face_har.xml')
face_detection_cordinates = face_harcascade.detectMultiScale(gray,1.1,3)
print(len(face_detection_cordinates))

# Making Bounding Box around the face

for x,y,w,h in face_detection_cordinates:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

##########################################################################################

# eyes detection through Harcascade

eye_harcascade = cv.CascadeClassifier('eye_har.xml')
eye_detection_cordinates = eye_harcascade.detectMultiScale(gray,1.1,3)
print(len(eye_detection_cordinates))

# Making Bounding Box around the eyes

for x,y,w,h in eye_detection_cordinates:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow('peoples',img)


cv.waitKey(0)
