# colorspace , BGR->HSV or BGR->GRAYSCALE
# 1) BGR->GRAYSCALE : cv2.cvtColor(img,flag) flag = COLOR_BGR2GRAY or COLOR_BGR2HSV
# HSV : Hue , Saturation and V : value range

import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

while 1:
	ret,frame=cap.read()

	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	# ranges for a color -> (color+-10,50-255,50-255)
	lower_blue=np.array([110,50,50])
	upper_blue=np.array([130,255,255])

	mask2=cv2.inRange(hsv,lower_blue,upper_blue)

	res=cv2.bitwise_and(frame,frame, mask = mask2)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask2)
	cv2.imshow('res',res)
	k=cv2.waitKey(5)&0xFF
	if k==ord('q'):
		break

cv2.destroyAllWindows()