import cv2 as cv
import numpy as np

##################read image
img = cv.imread('p/1.jpg')
cv.imshow('cat',img)
cv.waitKey(0)

##################grey
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey_cat',grey)
cv.waitKey(0)

##################resized
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)
cv.waitKey(0)

###################crop
crop = resized[0:300,0:400]
cv.imshow('croped',crop)
cv.waitKey(0)

###################Edge detection
edges = cv.Canny(resized,125,175)
cv.imshow('edges',edges)
cv.waitKey(0)

####################blur
blur = cv.GaussianBlur(resized,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blured',blur)
cv.waitKey(0)

###################dilate
dilate = cv.dilate(edges,(7,7),iterations=3)
cv.imshow('dilated',dilate)
cv.waitKey(0)

###################erode
erode = cv.erode(dilate,(7,7),iterations=3)
cv.imshow('eroded',erode)
cv.waitKey(0)