"""
    This program is created to create a text file named bg.txt that contains the names of all negative images.
"""
import glob
with open('bg.txt', 'w') as bg_file:
    for img in glob.glob("./negatives/**/*.jpg"):
        bg_file.write(img + '\n')
    bg_file.close()
