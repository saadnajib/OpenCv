import cv2 as cv
import numpy as np
blank = np.zeros((400,400),'uint8')

rectangle = cv.rectangle(blank.copy(),(20,20),(380,380),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise_and operations
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

#bitwise_or operations
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

#bitwise_not operations
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not',bitwise_not)

#bitwise_XOR operations
bitwise_XOR = cv.bitwise_xor(circle,rectangle)
cv.imshow('bitwise_xor',bitwise_XOR)

cv.waitKey(0)