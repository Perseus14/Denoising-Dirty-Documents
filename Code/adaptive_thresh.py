import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read the Image from the train folder
data = "../Data/"

testfile=open(data+"test.txt")

for x in testfile.readlines():
	img = cv2.imread(data+x[:-1],0)
	#Adaptive Thresholding - MEAN seems to be best with 11 block size and 2 constant
	thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
	cleaned_file = "adaptive_thresh/"+str(x.split('.')[0].split('/')[1])+"_cleaned.jpg"
	print cleaned_file
	print cv2.imwrite(cleaned_file,thresh2);

