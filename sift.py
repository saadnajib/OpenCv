import cv2 as cv

##################read image
img = cv.imread('p/5.jpg',cv.IMREAD_GRAYSCALE)
cv.imshow('book',img)

######################SIFT Feature detection

# sift = cv.xfeatures2d.SIFT_create()
# key_points,descriptors = sift.detectAndCompute(img,None)
#print(key_points)
#print(descriptors)

#####################SURF (Patented hence need licence) Feature detection
# surf = cv.xfeatures2d.SURF_create()
# key_points,descriptors = surf.detectAndCompute(img,None)

#####################orb Feature detection
orb = cv.ORB_create(nfeatures=1500)
key_points,descriptors = orb.detectAndCompute(img,None)

######################Draw Key Points
image = cv.drawKeypoints(img,key_points,None)
cv.imshow('sift',image)


cv.waitKey(0)
