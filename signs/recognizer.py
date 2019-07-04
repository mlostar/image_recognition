import cv2
cascade_right = cv2.CascadeClassifier('data/cascade.xml')
cascade_left = cv2.CascadeClassifier('data_left/cascade.xml')
cascade_stop = cv2.CascadeClassifier('data_stop/cascade.xml')
cap  = cv2.VideoCapture(0)
fontscale = 0.8
color = (255, 0, 0)
fontface = cv2.FONT_HERSHEY_PLAIN
while True:
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sign_right = cascade_right.detectMultiScale(gray)
    sign_left =  cascade_left.detectMultiScale(gray)
    sign_stop = cascade_stop.detectMultiScale(gray)
    for (x,y,w,h) in sign_stop:
        cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        cv2.putText(img,'stop', (x, y), fontface, fontscale, color)
    for (x, y, w, h) in sign_left:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.putText(img,'left_turn', (x, y), fontface, fontscale, color)
    for (x, y, w, h) in sign_right:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        cv2.putText(img,'right_turn', (x, y), fontface, fontscale, color)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) &0xff
    if k ==27:
        break
cap.release()
cv2.destroyAllWindows()