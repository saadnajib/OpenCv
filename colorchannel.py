import cv2 as cv
import numpy as np

img = cv.imread('p/3.jpg')
cv.imshow('bgr',img)

b,g,r = cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge = cv.merge([b,g,r])
cv.imshow('merged',merge)

#if we want to see blue, green, red colors

blank = np.zeros(img.shape[:2],'uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(blue.shape)
print(green.shape)
print(red.shape)

cv.waitKey(0)