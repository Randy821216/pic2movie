import os
import cv2
import numpy as np

path = './pics/'
filelist = os.listdir(path)
total_num = len(filelist)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
img_w = 512
img_h = 512

video=cv2.VideoWriter("VideoTest.avi",  fourcc, 20.0, (img_w, img_h))
for item in filelist:
	if item.endswith('.jpg'):
		item='./pics/'+item
		img1 = cv2.imread(item)
		img1 = cv2.resize(img1, (img_w, img_h))
		print(item)


		video.write(img1)
		cv2.imshow("Image", img1)
		key=cv2.waitKey(100)


video.release()
cv2.destroyAllWindows()

#************
#CODE_TYPE = 0   => no compression
#CODE_TYPE = -1  => jump out a msgbox asking for the compress formate
#=======================================
#CODE_TYPE = cv.CV_FOURCC(X,X,X,X)
#=======================================
#cv.CV_FOURCC('H','F','Y','U') # HuffYUV
#cv.CV_FOURCC('D','R','A','C') # BBC Dirac
#cv.CV_FOURCC('X','V','I','D') # MPEG-4 Part 2
#cv.CV_FOURCC('X','2','6','4') # MPEG-4 Part 10 (aka. H.264 or AVC)
#cv.CV_FOURCC('M','P','1','V') # MPEG-1 video
