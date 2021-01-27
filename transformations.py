import cv2 as cv
import numpy as np

img = cv.imread("p/1.jpg")
cv.imshow('img',img)

#resize

resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)

#flip

flip = cv.flip(resized,1)
cv.imshow('flip',flip)

#crop

cropped = resized[0:200,0:500]
cv.imshow('cropped',cropped)

#rotate

def img_rotation(img,angle,rotpoint=None):
    height,width = img.shape[:2]
    if  rotpoint == None:
        rotpoint = (width//2,height//2)
    dim = (height,width)
    rotate = cv.getRotationMatrix2D(rotpoint,angle,1)
    return cv.warpAffine(img,rotate,dim)

rotated = img_rotation(resized,45)
cv.imshow('rotated',rotated)

#transitions

def transitions(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    height,width = img.shape[:2]
    dim = (height,width)
    return cv.warpAffine(img,transmat,dim)

#-x = left
# x = right
# -y = up
# y = down

tran = transitions(resized,100,-100)
cv.imshow('move',tran)

cv.waitKey(0)



