import csv
import re
import cv2
import numpy as np
import copy

with open('rand_real.csv', 'rb') as f:
	reader = csv.reader(f)
	img=[]
	flag =False
	s,r,c = 0,0,0
	temp=[]
	for row in reader:
		if(row[0]=="id"):
			continue
		iid,val = row[0],int(float(row[1])*255)
		prev_s,prev_r,prev_col = s,r,c	
		s,r,c = map(int,iid.split('_'))	
		if(not flag):
			prev_s,prev_r,prev_c = s,r,c
		if(s!=prev_s):
			img1 = np.empty([len(img),len(img[1])])
			for x in xrange(len(img)):
				for y in xrange(len(img[1])):
					img1[x][y] = img[x][y]
					
			cv2.imwrite("rand/"+str(prev_s)+"_real_cleaned.jpg",img1)
			img = []
		elif(r!=prev_r):
			print s,r,c,prev_s,prev_r,prev_c
			#print temp
			img.append(copy.copy(temp))
			temp = []			
		else:
			#print temp
			temp.append(val)
		
		flag = True
