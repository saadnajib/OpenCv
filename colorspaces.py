import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('p/3.jpg')
cv.imshow('bgr',img)


#BGR to gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR to lab
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to HSV
HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',HSV)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

#plt.imshow(img)
#plt.imshow(rgb)
#plt.show()


#LAB to BGR
bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('bgr',bgr)

#for gray to lab we first need to convert it to bgr

cv.waitKey(0)