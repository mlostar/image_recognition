import cv2
import time
import sys
cascadeList=[]
WAIT=5
general_cascade=cv2.CascadeClassifier("./crc_out/cascade.xml")
with open('./cascade.txt',"rt") as file:
    for line in file:
        x=line.split("--")
        if(sys.platform.startswith('win')):
            x[1]=x[1][:-1]
        cascadeList.append([cv2.CascadeClassifier(x[0]),x[1]])
cap  = cv2.VideoCapture(0)
fontscale = 1.2
color = (255, 0, 0)
fontface = cv2.FONT_HERSHEY_PLAIN
cap.set(cv2.CAP_PROP_FPS,24)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,360)
ret ,img = cap.read()
start_time=time.time()
def subSignFinder(roiList,cascadeList,img):
    for roi in roiList:
        for cascade in cascadeList:
            sign=cascade[0].detectMultiScale(roi[0])
            for a in sign:
                #cv2.circle(img, (x+w//2,y+h//2), int(w+h)//4,(0,255,0),2)
                cv2.putText(img,cascade[1], (roi[1],roi[2]), fontface, fontscale, color)
while 1:
    roi_gray_list=[]
    roi_color_list=[]
    #response = "No detection"
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sign = general_cascade.detectMultiScale(img)
    for (x,y,w,h) in sign:
        #response  = "stop"
        cv2.circle(img, (x+w//2,y+h//2), int(w+h)//4,(0,255,0),2)
        roi_gray_list.append([gray[y:y+h,x:x+w],x,y])
        roi_color_list.append([img[y:y+h,x:x+w],x,y])
        #cv2.putText(img,'stop', (x, y), fontface, fontscale, color)
    subSignFinder(roi_gray_list,cascadeList,img)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) &0xff
    if k ==27:
        break
cap.release()
cv2.destroyAllWindows()
