import cv2
import numpy as np
cascade = cv2.CascadeClassifier('data/cascade.xml')
cap  = cv2.VideoCapture(0)
while True:
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sign = cascade.detectMultiScale(gray)
    for (x,y,w,h) in sign:
        cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
    cv2.imshow('img',img)
    k = cv2.waitKey(30) &0xff
    if k ==27:
        break
cap.release()
cv2.destroyAllWindows()