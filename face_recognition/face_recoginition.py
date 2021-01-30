import cv2 as cv
import numpy as np
import os


face_harcascade = cv.CascadeClassifier('front_face_har.xml')

trained_faces = np.load('faces_trained.yml',allow_pickle=True)