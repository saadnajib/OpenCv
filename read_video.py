import cv2 as cv

video = cv.VideoCapture(0)
while True:
    isTrue, frame = video.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()
