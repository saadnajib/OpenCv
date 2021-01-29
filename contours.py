import cv2 as cv
import numpy as np


img = cv.imread('p/3.jpg')
cv.imshow('cat',img)

################################################### Contours through Canny Filter 

canny = cv.Canny(img,125,125)

cv.imshow('canny',canny)

contour, herarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contour))

blank = np.zeros(img.shape,'uint8')
cv.imshow('blank',blank)

cv.drawContours(blank,contour,-1,(0,255,0),1)
cv.imshow('contour drawn',blank)

################################################### Contours through thresholding 

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# ret,thresh = cv.threshold(gray,180,255,cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)

# contour, herarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(len(contour))

# cv.drawContours(blank,contour,-1,(0,255,0),1)
# cv.imshow('contour drawn',blank)

cv.waitKey(0)