import numpy as np
import cv2
from matplotlib import pyplot as plt

data = "../Data/train/"
data1 = "../Data/train_cleaned/"
for x in xrange(2,100):
	img = cv2.imread(data+str(x)+".png",0)
	img1 = cv2.imread(data1+str(x)+".png",0)
	if(img==None or img1==None):
		continue	
	img_c=img.copy()
	hist = cv2.calcHist([img],[0],None,[256],[0,256])
	hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
	L=[]	
	for x in xrange(255):
		L.append([int(hist1[x]),x])
	L.sort()
	for x in L[::-1]:
		print x
	
	for x in xrange(img_c.shape[0]):
		for y in xrange(img_c.shape[1]):
			if(img_c[x][y]>=50 and img_c[x][y]<=150):
				continue
			else:
				img_c[x][y]=255
			
	hist2 = cv2.calcHist([img_c],[0],None,[256],[0,256])
	plt.subplot(321),plt.imshow(img,'gray')
	plt.subplot(322),plt.plot(hist),plt.xlim([-10,256])
	plt.subplot(323),plt.imshow(img1,'gray')
	plt.subplot(324),plt.plot(hist1),plt.xlim([-10,256])
	plt.subplot(325),plt.imshow(img_c,'gray')
	plt.subplot(326),plt.plot(hist2),plt.xlim([-10,256])
	plt.show()
	plt.close()
