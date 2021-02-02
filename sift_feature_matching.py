import cv2 as cv

##################read image
img1 = cv.imread('p/6.jpg',cv.IMREAD_GRAYSCALE)
img2 = cv.imread('p/9.jpg',cv.IMREAD_GRAYSCALE)
img1 = cv.resize(img1,(500,500),interpolation=cv.INTER_LINEAR)
img2 = cv.resize(img2,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('house1',img1)
cv.imshow('house2',img2)

######################SIFT Feature detection

# sift = cv.xfeatures2d.SIFT_create()
# key_points1,descriptors1 = sift.detectAndCompute(img1,None)
# key_points2,descriptors2 = sift.detectAndCompute(img2,None)
#print(key_points)
#print(descriptors)

#####################SURF (Patented hence need licence) Feature detection
# surf = cv.xfeatures2d.SURF_create()
# key_points,descriptors = surf.detectAndCompute(img,None)

#####################orb Feature detection
orb = cv.ORB_create(nfeatures=1500)
key_points1,descriptors1 = orb.detectAndCompute(img1,None)
key_points2,descriptors2 = orb.detectAndCompute(img2,None)

########################Brute Force Matching
bf = cv.BFMatcher(cv.NORM_HAMMING,crossCheck=True)
matches = bf.match(descriptors1,descriptors2)
matches = sorted(matches,key= lambda X:X.distance)

######################Draw Matches
matches_result = cv.drawMatches(img1,key_points1,img2,key_points2,matches[:20],None)
cv.imshow('sift',matches_result)

cv.waitKey(0)
