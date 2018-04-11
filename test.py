import numpy as np
import cv2

#this is the cascade we just made. Call what you want
watch_cascade = cv2.CascadeClassifier('/home/ganesh/opencv-3.1.0/data/haarcascades/ear.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    watches= watch_cascade.detectMultiScale(img, 1.5,7)
    for (x,y,w,h) in watches:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
	roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
