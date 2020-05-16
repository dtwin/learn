#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('c01.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,60,255,0)
image ,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#绘制独立轮廓，如第四个轮廓
#imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
#但是大多数时候，下面方法更有用
imag = cv2.drawContours(img,contours,-1,(0,255,0),3)

cnt=contours[0]
M=cv2.moments(cnt)
print(M)
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
area=cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt,True)

epsilon=0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)#将轮廓形状近似到另外一种由更少点组成的轮廓形状

#hull = cv2.convexHull(points,hull,clockwise,returnPoints)#函数cv2.convexHull()可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷。
#hull=cv2.convexHull(cnt)

#（x,y）为矩形左上角的坐标，（w,h）是矩形的宽和高
x,y,w,h=cv2.boundingRect(cnt)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

ellipse = cv2.fitEllipse(cnt)
img = cv2.ellipse(img,ellipse,(0,255,0),2)

#直线拟合
rows,cols = img.shape[:2]
[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
lefty=int((x*vy/vx)+y)
righty=int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

while(1):
    cv2.imshow('img',img)
    cv2.imshow('thresh',thresh)
    cv2.imshow('imgray',imgray)
    cv2.imshow('image',image)
    cv2.imshow('imag',imag)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()