import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def invert(img):
	return 255-img

#Read the Image from the train folder
for fname in os.listdir('../Data/test_real/'):
	name = fname
	fname = os.path.join('../Data/test_real', fname)
	img = cv2.imread(fname,0)	

	median = cv2.medianBlur(img,17)

	#Subtracting Background
	img_int = img.astype(int)
	med_int = median.astype(int)
	res2 = median - img

	for i in xrange(img.shape[0]):
		for j in xrange(img.shape[1]):
			med_int[i][j] = med_int[i][j] + 150

	res = med_int - img_int
	for i in xrange(img.shape[0]):
		for j in xrange(img.shape[1]):
			if (res[i][j] > 255): 
				res[i][j] = 255
	res = res.astype(np.uint8)

	#Results shown as follows

	#cv2.imwrite('med_res_final.png', res)
	#cv2.imwrite('background.png', median)
	#cv2.imwrite('med_res.png', res2)
	
	cleaned_file = "median/"+str(name.split('.')[0])+"_real_cleaned.jpg"
	print cleaned_file
	print cv2.imwrite(cleaned_file,invert(res));

