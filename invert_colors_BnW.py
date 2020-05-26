import cv2
import os
import imghdr

directory = input("Enter the absolute path of the directory\n")

os.chdir(directory)
try:
    os.mkdir("inverted")
except FileExistsError:
    print('File already exists, thus using the same file.')

print("Processing .....")
for img_file in os.listdir("."):

    if img_file.split(".")[-1] not in ['jpg','png','jpeg']:
        continue

    image = cv2.imread(img_file)
    image = ~image
    new_name = img_file.split(".")[0]+"_inverted."+img_file.split(".")[1]
    cv2.imwrite("./inverted/"+new_name, image)

print("Done.... The images are stored in inverted/ folder")