import cv2 as cv

img = cv.imread('p/4.jpg')
cv.imshow('cat',img)

# Averageing blur
avg_blur = cv.blur(img,(7,7))
cv.imshow('avg_blur',avg_blur)

# Gassuian blur
gaus_blur = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaus_blur',gaus_blur)

#Median blur
median_blur = cv.medianBlur(img,7)
cv.imshow('median_blur',median_blur)

#Bilateral blur
bi_blur = cv.bilateralFilter(img,10,100,10)
cv.imshow('bi_blur',bi_blur)

cv.waitKey(0)