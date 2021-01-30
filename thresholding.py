import cv2 as cv

img = cv.imread('p/4.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Thresholding

threshold, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
print(threshold)
cv.imshow('thresholding',thresh)

# Inverse Thresholding

threshold, thresh_inv = cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)
print(threshold)
cv.imshow('thresholding_inv',thresh_inv)

# Adaptive Thresholding

ad_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
print(threshold)
cv.imshow('Adaptive_thresholding',ad_thresh)

# Adaptive Thresholding Inverse

ad_thresh_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
print(threshold)
cv.imshow('Adaptive_thresholding_inverse',ad_thresh_inv)


cv.waitKey(0)