import numpy as np
import cv2
from matplotlib import pyplot as plt

data = "../Data/"
#data1 = "../Data/train_cleaned/"
testfile=open(data+"test.txt")
for x in testfile.readlines():
	img = cv2.imread(data+x[:-1],0)
	#img1 = cv2.imread(data1+str(x)+".png",0)
	#if(img==None or img1==None):
	#	continue	
	print data+x
	img_c=img.copy()
	hist = cv2.calcHist([img],[0],None,[256],[0,256])
	#hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
	#L=[]	
	#for i in xrange(255):
	#	L.append([int(hist1[i]),i])
	#L.sort()
	#for x in L[::-1]:
	#	print x
	
	for i in xrange(img_c.shape[0]):
		for j in xrange(img_c.shape[1]):
			if(img_c[i][j]>=50 and img_c[i][j]<=150):
				continue
			else:
				img_c[i][j]=255
	cleaned_file = "prelim1/"+str(x.split('.')[0].split('/')[1])+"_cleaned.jpg"
	print cleaned_file
	#hist2 = cv2.calcHist([img_c],[0],None,[256],[0,256])
	print cv2.imwrite(cleaned_file,img_c);
	'''	
	plt.subplot(321),plt.imshow(img,'gray'),plt.xticks([]),plt.yticks([])
	plt.subplot(322),plt.plot(hist),plt.xlim([-10,256]),plt.yticks([])
	plt.subplot(323),plt.imshow(img1,'gray'),plt.xticks([]),plt.yticks([])
	plt.subplot(324),plt.plot(hist1),plt.xlim([-10,256]),plt.yticks([])
	plt.subplot(325),plt.imshow(img_c,'gray'),plt.xticks([]),plt.yticks([])
	plt.subplot(326),plt.plot(hist2),plt.xlim([-10,256]),plt.yticks([])
	plt.tight_layout()	
	plt.savefig(str(x)+"_cleaned.jpg")
	plt.close()
	'''
