import cv2
import time
cascade_right = cv2.CascadeClassifier('../signs/data/cascade.xml')
cascade_left = cv2.CascadeClassifier('../signs/data_left/cascade.xml')
cascade_stop = cv2.CascadeClassifier('../signs/data_stop/cascade.xml')
#video capture settings
cap  = cv2.VideoCapture(0)
fontscale = 0.8
color = (255, 0, 0)
fontface = cv2.FONT_HERSHEY_PLAIN
cap.set(cv2.CAP_PROP_FPS,Frame_rate)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,180)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,180)
ret,img = cap.read()
#append your cascades in this list
cascade_list[cascade_right,cascade_left,cascade_right]
def isEmpty(a):
    """
     chechks if given variable is empty or not
     takes 1 argument in all types
    returns boolean value
    """
    try:
        if(a):
            return True
        else :
            return False
    except:
        return True
def which_sign(n):
    """
    finds traffic signs in an image
    takes 1 argument, an integer that specifies the cascade
    returns 1 byte long bytes
    """
    if n > len(cascade_list):
        print("this cascade is not in the list")
        return b'x00'
    sign=[]
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if(n):
        sing=cascade_list[n].detectMultiScale(gray)
        if(is_empty(sign[n]):
            return b'x00'
        else:
            return b'x01'
