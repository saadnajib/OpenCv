import cv2 as cv

###################################################functions

def rescale_video_img(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width,height)
    return (cv.resize(frame,dim,interpolation=cv.INTER_AREA))

def capture_video_recale(capture,height,width):
    
    capture.set(3,width)
    capture.set(4,height)


####################################################read video
video = cv.VideoCapture(0)

#capture_video_recale(video,100,100)

while True:
    isTrue, frame = video.read()
    
    frame = rescale_video_img(frame,0.2)
   
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()


##################################################read image
img = cv.imread('p/2.jpg')
#cv.imshow('cat',img)
rescaled_img = rescale_video_img(img,0.5)
cv.imshow('cat',rescaled_img)
cv.waitKey(0)



