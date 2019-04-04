import cv2
import numpy as np

#READING THE IMAGE
img = cv2.imread('MyPic.png')
print(img.item(0,0,0)) #prints the value of the corresponding pixel

img.itemset((0,0,0),255) #changing the value of the corresponding pixel to 255
print(img.item(0,0,0))    #prints the value 255
