#!/usr/bin/env python
#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('c01.jpg',0)
kernel = np.ones((5,5),np.uint8) #之前的例子都是使用numpy构建了结构化元素，但是是正方形的，若需要构建椭圆或者圆形的核，可以使用OpenCV提供的函数cv2.getStructuringElemenet()，只需要告诉它你需要的核的形状和大小。
#cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) 椭圆
#cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) 矩形
#cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) 圆形
erosion = cv2.erode(img,kernel,iterations=1) #腐蚀
#dilation = cv2.dilation(img,kernel,iterations=1) #膨胀
#opening = cv2.morphotogyEx(img,cv2.MORPH_OPEN,kernel) 先进行腐蚀再进行膨胀就叫做开运算。被用来去除噪音，函数可以使用cv2.morphotogyEx()
#closing = cv2.morphotogyEx(img,cv2.MORPH_CLOSE,kernel) 先膨胀再腐蚀。被用来填充前景物体中的小洞，或者前景上的小黑点。
#gradient = cv2.morphotogyEx(img,cv2.MORPH_GRADIENT,kernel) 其实就是一幅图像膨胀与腐蚀的差别。结果看上去就像前景物体的轮廓。
#tophat = cv2.morphotogyEx(img,cv2.MORPH_TOPHAT,kernel) 礼帽——原始图像与进行开运算之后得到的图像的差。
#blackhat = cv2.morphotogyEx(img,cv2.MORPH_BLACKHAT,kernel) 黑帽——进行闭运算之后得到的图像与原始图像的差。
while(1):
    cv2.imshow('image',img)
    cv2.imshow('erosion',erosion)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()