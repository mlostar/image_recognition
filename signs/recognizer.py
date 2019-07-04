import cv2
import time
cascade_right = cv2.CascadeClassifier('data/cascade.xml')
cascade_left = cv2.CascadeClassifier('data_left/cascade.xml')
cascade_stop = cv2.CascadeClassifier('data_stop/cascade.xml')
cap  = cv2.VideoCapture(0)
fontscale = 0.8
color = (255, 0, 0)
fontface = cv2.FONT_HERSHEY_PLAIN
cap.set(cv2.cv.CV_CAP_PROP_FPS,24)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,180)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,180)
ret ,img = cap.read()
imgarr=[]
start_time=time.time()
while time.time()-start_time<10:
    #response = "No detection"
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sign_right = cascade_right.detectMultiScale(gray)
    sign_left =  cascade_left.detectMultiScale(gray)
    sign_stop = cascade_stop.detectMultiScale(gray)
    for (x,y,w,h) in sign_stop:
        #response  = "stop"
        cv2.circle(img, (x+w/2,y+h/2), (w+h)/4,(0,255,0),2)
        #roi_gray = gray[y:y+h,x:x+w]
        #roi_color = img[y:y+h,x:x+w]
        cv2.putText(img,'stop', (x, y), fontface, fontscale, color)
    for (x, y, w, h) in sign_left:
        #response = "sign_left"
        cv2.circle(img, (x+w/2,y+h/2), (w+h)/4, (0, 255, 0), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        #roi_color = img[y:y + h, x:x + w]
        cv2.putText(img,'left_turn', (x, y), fontface, fontscale, color)
    for (x, y, w, h) in sign_right:
        #response = "sign_right"
        cv2.circle(img, (x+w/2,y+h/2), (w+h)/4, (0, 255, 0), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        #roi_color = img[y:y + h, x:x + w]
        cv2.putText(img,'right_turn', (x, y), fontface, fontscale, color)
    #if response is not "No detection":
     #   print(response)    
    #cv2.imshow('img',img)
    imgarr.append(img)
    k = cv2.waitKey(30) &0xff
    if k ==27:
        break
out = cv2.VideoWriter('project.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 24, (180,180))
for im in imgarr:
    out.write(im)
out.release()
cap.release()
cv2.destroyAllWindows()
