import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read the Image from the train folder
img = cv2.imread('../Data/train/2.png',0)
#img = cv2.medianBlur(img,5)

#Fixed Thresholding with 'threshold value' as 170 (Ideal range is from 165-175)
ret,thresh1 = cv2.threshold(img,170,255,cv2.THRESH_BINARY)

#Adaptive Thresholding - MEAN seems to be best with 11 block size and 2 constant
thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

#Canny Edge Detection with 100 400 seems to be the best - but actually the more you increase the more goes away
edges = cv2.Canny(img,100,200)

#Erosion and Dilation
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(edges,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)


cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Edge Images', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Morphology/2-dilation.png',dilation)

