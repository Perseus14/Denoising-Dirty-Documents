from os import listdir
from os.path import isfile, join
import cv2
import csv

#Code to convert the outputs of the methods in csv format for submission in Kaggle
mypath=raw_input()+"/"
img_names = [f for f in listdir(mypath) if f.endswith(".jpg") if isfile(join(mypath, f))]
img_names.sort(key=lambda x:int(x.split('_')[0]))

#print img_names
print "id,value"
for x in img_names:
	img=cv2.imread(mypath+x,0);
	for j in xrange(img.shape[1]):
		for i in xrange(img.shape[0]):
			print "%s,%d"%(x.split('_')[0]+"_"+str(i+1)+"_"+str(j+1), img[i][j])
