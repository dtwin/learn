#!/usr/bin/env python
#-*- coding:utf-8 -*-
import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('c01.jpg',0)
edges = cv2.Canny(img,50,100)

while(1):
    cv2.imshow('edges',edges)
    cv2.imshow('img',img)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()

#plt.subplot(121),plt.imshow(img,cmap='gray')
#plt.title('original'),plt.xticks([]),plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap='gray')
#plt.title('edge'),plt.xticks([]),plt.yticks([])

#plt.show()