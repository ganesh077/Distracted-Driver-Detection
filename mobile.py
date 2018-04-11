import numpy as np
import cv2
import pyglet
face_cascade = cv2.CascadeClassifier('13stagecascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 8)

    if list(faces):
	sound=pyglet.resource.media('sound91.wav',streaming=False)
	sound.play()
	
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
