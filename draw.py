import cv2 as  cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
cv.waitKey(0)

blank[0:300,300:400]=(10,255,0)
cv.imshow('fill',blank)
cv.waitKey(0)

cv.rectangle(blank,(0,0),(250,250),(0,255,220),thickness=cv.FILLED)
cv.imshow('rectangle',blank)
cv.waitKey(0)

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,0,255),thickness=-1)
cv.imshow('circle',blank)
cv.waitKey(0)

cv.putText(blank,'hello saad here',(0,blank.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1,(255,255,255),thickness=1)
cv.imshow('text',blank)
cv.waitKey(0)

cv.line(blank,(blank.shape[1]//2,blank.shape[0]//2),(0,250),(255,255,255),thickness=3)
cv.imshow('line',blank)
cv.waitKey(0)
