import numpy as np
import cv2

img = cv2.imread('c01.jpg')
lower_reso = cv2.pyrDown(img)
higher_reso2 = cv2.pyrUp(img)

while(1):
    cv2.imshow('img',img)
    cv2.imshow('lower_reso',lower_reso)
    cv2.imshow('higher_reso2',higher_reso2)
    if cv2.waitKey() == ord('q'):
        break
cv2.destroyAllWindows()