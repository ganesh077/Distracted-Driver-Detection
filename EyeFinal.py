import numpy as np
import cv2
import pyglet
eye_cascade = cv2.CascadeClassifier('/home/ganesh/opencv-3.1.0/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(0)
while 1:
	ret,img=cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = eye_cascade.detectMultiScale(gray, 1.5,3)
	print faces
	faces1=list(faces)
	if faces1:
	    	for (x,y,w,h) in faces1:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
	    		cv2.imshow('img',img)
	    	
	elif not faces1:
		sound=pyglet.resource.media('sound84.wav',streaming=False)
		sound.play()
	    	

cv2.destroyAllWindows()
