import cv2
import numpy as np
img = cv2.imread('/home/pi/camera/found/c01.jpg')
#px = img[100,100]
#print(px)
#blue = img[100,100,0]
#print(blue)
#img[101,101]=[255,255,255]
#print(img[101,101])
print(img.shape)
print(img.size)

b=img[:,:,0]
print(b)

print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))