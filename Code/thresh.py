import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read the Image from the train folder
data = "../Data/"

testfile=open(data+"test.txt")

for x in testfile.readlines():
	img = cv2.imread(data+x[:-1],0)

	#Fixed Thresholding with 'threshold value' as 170 (Ideal range is from 165-175)
	ret,thresh1 = cv2.threshold(img,170,255,cv2.THRESH_BINARY)

	cleaned_file = "thresh/"+str(x.split('.')[0].split('/')[1])+"_cleaned.jpg"
	print cleaned_file
	#print cv2.imwrite(cleaned_file,thresh1);
