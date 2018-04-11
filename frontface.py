import numpy as np
import cv2
import pyglet
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('/home/ganesh/opencv-3.1.0/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if list(faces):
    	for (x,y,w,h) in faces:
        	roi_gray = gray[y:y+h, x:x+w]
        	eyes = eye_cascade.detectMultiScale(roi_gray)
		if not list(eyes):		        	
			sound=pyglet.resource.media('sound84.wav',streaming=False)
			sound.play()			
			
cap.release()
cv2.destroyAllWindows()


