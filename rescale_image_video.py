import cv2 as cv

img = cv.imread('p/1.jpg')
cv.resize(img,28,28)
cv.imshow('cat',img)
cv.waitKey(0)
