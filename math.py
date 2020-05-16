import cv2
import numpy as np
img1=cv2.imread('1.png')
img2=cv2.imread('2.png')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
print(dst)
img2=cv2.imwrite('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
