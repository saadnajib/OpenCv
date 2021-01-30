import cv2 as cv
import numpy as np

img = cv.imread('p/3.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# laplacian edge detection 

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

# sobel edge detection

sobel_x= cv.Sobel(gray,cv.CV_64F,1,0)
cv.imshow('sobel_x',sobel_x)

sobel_y= cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobel_y',sobel_y)

sobel = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('sobel',sobel)

# canny edge detection

canny = cv.Canny(img,150,175)
cv.imshow('canny',canny)


cv.waitKey(0)