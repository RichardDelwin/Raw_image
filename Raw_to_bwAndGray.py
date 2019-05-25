import numpy
import PIL
import rawpy
import scipy
import imageio
import mpldatacursor
import matplotlib.pyplot as plt

path = 'C:\\Users\\RichardDel\\Desktop\\TheOne.dng'
img = rawpy.imread(path)            #to read a raw file
narray = img.postprocess()  #3D array
r,c,e = narray.shape    #r-rows, c-columns, e-elements

#creating to copies of 'narray' in which one of them is used for grayscale images 
# and the other for b/w or binary image 

narr1 = numpy.copy(narray)
narr2 = numpy.copy(narray)

cc=0    #counter , just to keep track of the progress made in the loop

#text file where the binary values would be writtten into
fp = open("C:\\Users\\RichardDel\\Desktop\\TheOneData.txt","w+")    

for row in range(0,r):
    buff =fp.write("\n")    #new line for every row of the image
    cc+=1           #the counter
    if cc%200==0:   #to display the progress for every 200 rows processed
        print(cc)

    for col in range(0,c):
#        count = 0
        avg = int((int(narr1[row,col,0])+int(narr1[row,col,1])+int(narr1[row,col,2]))/3)    #grayscale value 
        if avg<128:                         #thresholding
            narr1[row][col]=[0,0,0]         #for binary image file --narr1
            buff = fp.write("0 ")           #text file
        else:
            narr1[row][col]=[255,255,255]
            buff = fp.write("1 ")
        narr2[row][col]=[avg]           #for grayscale image file --narr2

imageio.imsave('C:\\Users\\RichardDel\\Desktop\\ResImgWithGrayScale.png',narr1)     # creating the grayscale image file from narr1
imageio.imsave('C:\\Users\\RichardDel\\Desktop\\ResImgWithGrayScale.bmp',narr2)     # creating the binary image file from narr2
fp.close()

#creation of the image viewer
data = narr1    #this one is for the binary image file  --- substitute narr1 with narr2 for grayscale file
fig, ax = plt.subplots()
ax.imshow(data, interpolation='none')

mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
plt.show()
