import cv2
import numpy as np
from matplotlib import pyplot as plt

def invert(img):
	return 255-img
#Read the Image from the train folder
data = "../Data/"

testfile=open(data+"test.txt")

for x in testfile.readlines():
	img = cv2.imread(data+x[:-1],0)
	#Canny Edge Detection with 100 400 seems to be the best - but actually the more you increase the more goes away
	edges = cv2.Canny(img,100,200)
	#edges = invert(edges)
	#Erosion and Dilation
	kernel = np.ones((3,3),np.uint8)
	dilation = cv2.dilate(edges,kernel,iterations = 1)
	erosion = cv2.erode(dilation,kernel,iterations = 1)
	
	'''
	cv2.imshow('Original Image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imshow('Edge Images', invert(edges))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imshow('Dilation', invert(dilation))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	cv2.imshow('Erosion', invert(erosion))
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	'''

	cleaned_file_dil = "canny/dil/"+str(x.split('.')[0].split('/')[1])+"_cleaned.jpg"
	print cleaned_file_dil
	print cv2.imwrite(cleaned_file_dil,invert(dilation));
	
	cleaned_file_ero = "canny/ero/"+str(x.split('.')[0].split('/')[1])+"_cleaned.jpg"
	print cleaned_file_ero
	print cv2.imwrite(cleaned_file_ero,invert(erosion));
