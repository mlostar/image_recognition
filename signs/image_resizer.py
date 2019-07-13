import cv2
import glob
filename = './'+input('output folder directory\n')+'/'+input("output file name\n")
input_file_directory='./'+input("input file directory\n")+"/**/*"
extension=input("image extension")
width=input("width")
height=input("height")
input_file_directory+=extension
counter = 0
params = " 1 0 0 "+str(width)+" "+str(height)
with open('info.lst', 'w') as info_file:
    for img in glob.glob(input_file_directory,recursive=True):
        image = cv2.imread(img)
        resized_image = cv2.resize(image,(int(width),int(height)),interpolation=cv2.INTER_AREA)
        resized_image=cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
        final_file_name = filename+  str(counter)+"."+extension
        cv2.imwrite(final_file_name,resized_image)
        counter+=1
        info_file.write(final_file_name + params +'\n')
    info_file.close()
