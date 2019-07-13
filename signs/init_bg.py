import glob
with open('bg.txt', 'w') as bg_file:
    for img in glob.glob("./negatives/**/*.jpg"):
        bg_file.write(img + '\n')
    bg_file.close()
