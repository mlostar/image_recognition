import cv2
import glob
filename = 'stop_'
counter = 0
params = " 1 0 0 25 25"
with open('info.lst', 'w') as info_file:
    for img in glob.glob("./dataset/14/*.png"):
        image = cv2.imread(img)
        resized_image = cv2.resize(image,(25,25),interpolation=cv2.INTER_AREA)
        final_file_name = filename+  str(counter)+".png"
        cv2.imwrite(final_file_name,resized_image)
        counter+=1
        info_file.write(final_file_name + params +'\n')
    info_file.close()



