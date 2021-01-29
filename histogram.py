import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('p/4.jpg')
cv.imshow('cat',img)

#grayscale image histogram

#converting imge to grayscale 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# displaying histogram

histogram = cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.plot(histogram)
plt.title('Gray Histogram without Masking')
plt.xlabel('no of bins')
plt.ylabel('no of pixels')
plt.show()

###################################################################################

# creating blank image and drawing a circle

blank = np.zeros(img.shape[:2],'uint8')
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),50,255,-1)

# masking circle on gray image

masked = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('masked',masked)

# displaying histogram

histogram = cv.calcHist([gray],[0],masked,[256],[0,256])
plt.figure()
plt.plot(histogram)
plt.title('Gray Histogram with Masking')
plt.xlabel('no of bins')
plt.ylabel('no of pixels')
plt.show()

#Colored image histogram
plt.figure()
plt.title('Colored Histogram without Masking')
plt.xlabel('no of bins')
plt.ylabel('no of pixels')

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])    
    plt.plot(hist,color=col)
    plt.xlim(0,256)

plt.show()

#Masked Colored image histogram

# circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),50,255,-1)
# colored_masked = cv.bitwise_and(img,img,mask=circle)
# cv.imshow('colored_masked',colored_masked)

# plt.figure()
# plt.title('Colored Histogram with Masking')
# plt.xlabel('no of bins')
# plt.ylabel('no of pixels')

# color = ('b','g','r')
# for i,col in enumerate(color):
#     histo = cv.calcHist([gray],[i],colored_masked,[256],[0,256])    
#     plt.plot(histo,color=col)
#     plt.xlim(0,256)

# plt.show()




cv.waitKey(0)