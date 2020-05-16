#!/usr/bin/env python
#-*- coding:utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

ret,thresh=cv2.threshold(img1,60,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img2,60,255,cv2.THRESH_BINARY)
_,contours,_ =cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt1=contours[0]
_,contours,_ =cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt2=contours[0]
ret=cv2.matchShapes(cnt1,cnt2,1,0,0)
print(ret)