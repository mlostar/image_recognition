import cv2
import numpy as np
import matplotlib
import time
#this is for my pc compatability
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
MAX_BLUR_LEVEL=3
BLR_COEFFICENT=3
MAX_BRIGHTNESS_LEVEL=5
BRR_COEFFICENT=15
MAX_SAMPLE=250
path=input("output directory:")
video_path=input("input video:")
cap= cv2.VideoCapture('./'+video_path)
JUMP=10
WIDTH=25
HEIGHT=50
i=0
FRAME_EXTEND=50
general_cascade=cv2.CascadeClassifier("../signs/outgray/cascade.xml")
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
def decrease_brightnes(img,value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v[v > value ] -= value
    v[v <= value] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
def circe_finder(img):
    img = img.astype('uint8')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,9)
    h = gray.shape[0]
    w = gray.shape[1]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, h // 1.5,param1=200, param2=40,minRadius=int(h/4), maxRadius=h//2)
    try:
        circles = np.uint16(np.around(circles))
        i=circles[0,0]
        roi=[max(int(i[0])-int(i[2]),0),max(int(i[1])-int(i[2]),0),2*i[2]]
    except:
    #    i=[0,0,0,0]
        roi=[0,0,0]
    #oi=[max(int(i[0])-int(i[2]),0),max(int(i[1])-int(i[2]),0),i[2]]
    #roi=[0,0,0,0]
    return roi
def data_create():
    j =0
    global MAX_BLUR_LEVEL,MAX_BLUR_LEVEL,JUMP,i,FRAME_EXTEND,MAX_SAMPLE,WIDTH,HEIGHT,BLR_COEFFICENT,BRR_COEFFICENT
    while(cap.isOpened()):
        if(j>MAX_SAMPLE):
            break
        ret, frame = cap.read()
        if ret == False:
            break
        #sign=general_cascade.detectMultiScale(frame)
        roi=circe_finder(frame)
        while cap.isOpened() and roi[2]==0:
            ret,frame=cap.read()
            if not ret:
                return
            roi=circe_finder(frame)
        (x,y,w,h)=(roi[0],roi[1],roi[2],roi[2])
        print((x,y,w,h))
        (a,b)=frame.shape[:2]
        print(a,b)
        frame=frame[max(y-FRAME_EXTEND,0):y+h+FRAME_EXTEND,max(x-FRAME_EXTEND,0):x+w+FRAME_EXTEND]
        (a,b)=frame.shape[:2]
        print(a,b)
        #M = cv2.getRotationMatrix2D((b/2,a/2), 270, 1)
        #frame2 = cv2.warpAffine(frame, M, (b,a))
        cv2.imshow('img',frame)
        k = cv2.waitKey(30) &0xff
        if k ==27:
            break
        if(w<100 or h <100):
            continue
        j+=1
        for blr in range(MAX_BLUR_LEVEL):
            blr=blr*BLR_COEFFICENT//2*2+1
            if(blr>3):
                blurred=cv2.medianBlur(frame,blr)
            else:
                blurred=frame
            for brr in range(MAX_BRIGHTNESS_LEVEL):
                brr*=BRR_COEFFICENT
                increased=increase_brightness(blurred,brr)
                increased=cv2.resize(increased,(int(WIDTH),int(HEIGHT)),interpolation=cv2.INTER_AREA)
                increased=cv2.cvtColor(increased,cv2.COLOR_BGR2GRAY)
                cv2.imwrite("./"+path+'/'+str(i)+".jpg",increased)
                i+=1
                decreased=decrease_brightnes(blurred,brr)
                decreased=cv2.resize(decreased,(int(WIDTH),int(HEIGHT)),interpolation=cv2.INTER_AREA)
                decreased=cv2.cvtColor(decreased,cv2.COLOR_BGR2GRAY)
                cv2.imwrite("./"+path+'/'+str(i)+".jpg",decreased)
                i+=1
        for a in range(JUMP):
            if(cap.isOpened()):
                ret,frame=cap.read()
    cap.release()
    cv2.destroyAllWindows()
    return
data_create()
