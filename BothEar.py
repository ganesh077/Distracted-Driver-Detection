import numpy as np
import cv2
import pyglet

right_ear = cv2.CascadeClassifier('/home/ganesh/opencv-3.1.0/data/haarcascades/ear_right.xml')
left_ear=cv2.CascadeClassifier('ear.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img1 = cap.read()
    img=cv2.flip(img1,1)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    faces = right_ear.detectMultiScale(gray, 1.5,3)
    faces1=list(faces)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
    faces2=left_ear.detectMultiScale(gray1,1.5,2)
    faces3=list(faces2)

     	
    if faces1 and not faces3:
    	sound=pyglet.resource.media('sound81.wav',streaming=False)
        sound.play()
    
    if faces3 and not faces1:
    	sound=pyglet.resource.media('sound91.wav',streaming=False)
        sound.play()
    	
		

    	k = cv2.waitKey(30) & 0xff
    	if k == 27:
       		break

cap.release()
cv2.destroyAllWindows()
