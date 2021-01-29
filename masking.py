import cv2 as cv
import numpy as np

img = cv.imread('p/4.jpg')
cv.imshow('cat',img)

blank = np.zeros(img.shape[:2],'uint8')

#creating a circle
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),50,255,-1)
cv.imshow('circle',circle)

#creating a rectangle
rectangle = cv.rectangle(blank.copy(),(20,20),(200,200),255,-1)
cv.imshow('rectangle',rectangle)

#creating a new shape from the above shapes
new_shape = cv.bitwise_or(circle,rectangle)

#masking on the new shape
masked = cv.bitwise_and(img,img,mask=new_shape)
cv.imshow('masked',masked)

cv.waitKey(0)