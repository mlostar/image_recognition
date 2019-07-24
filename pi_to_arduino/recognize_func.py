import cv2
import time
cascade_right = cv2.CascadeClassifier('../signs/data/cascade.xml')
cascade_left = cv2.CascadeClassifier('../signs/data_left/cascade.xml')
cascade_stop = cv2.CascadeClassifier('../signs/data_stop/cascade.xml')
cap  = cv2.VideoCapture(0)
fontscale = 0.8
color = (255, 0, 0)
Frame_rate=3
fontface = cv2.FONT_HERSHEY_PLAIN
cap.set(cv2.CAP_PROP_FPS,Frame_rate)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,180)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,180)
ret,img = cap.read()
cascade_list[cascade_right,cascade_left,cascade_right]
def isEmpty(a):
    try:
        if(a):
            return True
        else :
            return False
    except:
        return True
def which_sign(n):
    sign=[]
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if(n):
        sing=cascade_list[n].detectMultiScale(gray)
        if(is_empty(sign[n]):
            return b'x00'
        else:
            return b'x01'
