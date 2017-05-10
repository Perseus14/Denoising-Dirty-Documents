import concurrent.futures
import csv
import logging
import random
import pickle

import joblib
import numpy as np
import sklearn.ensemble
import sklearn.cross_validation
import sklearn.metrics

import skimage.data

from pathlib import Path

from PIL import Image as image

TRAIN_DIR = Path("../Data/train/")
TARGET_DIR = Path("../Data/train_cleaned/")
TEST_DIR = Path("../Data/test_real/")

CHUNKSIZE = 3000000

logging.basicConfig(level=logging.INFO)

def get_padded(imgarray, padding=1):
    padval = int(round(imgarray.flatten().mean()))
    rows, cols = imgarray.shape
    xpad = np.full((rows, padding), padval, dtype='uint8')
    ypad = np.full((padding, cols + 2 * padding), padval, dtype='uint8')
    return np.vstack((ypad, np.hstack((xpad, imgarray, xpad)), ypad))

def get_features_for_image(imgarray, padding=1):
    rows, cols = imgarray.shape
    padded = get_padded(imgarray, padding=padding)
    features = []
    return np.vstack(tuple(
        np.vstack(tuple(
            padded[i: i + 2 * padding + 1, j: j + 2 * padding + 1].reshape((1, -1))
            for j in range(cols)
        )) for i in range(rows)
    ))

def get_features_for_path(path, padding=1):
    return get_features_for_image(skimage.data.imread(str(path),as_grey=True), padding=padding)

def get_target_for_path(path):
    return skimage.data.imread(str(path),as_grey=True).flatten() / 255

def get_training_sets():
    X = list(joblib.Parallel(n_jobs=-1)(
        joblib.delayed(get_features_for_path)(i)
        for i in TRAIN_DIR.iterdir()))
    y = list(joblib.Parallel(n_jobs=-1)(
        joblib.delayed(get_target_for_path)(i)
        for i in TARGET_DIR.iterdir()))
    X = np.concatenate(X)
    y = np.concatenate(y)
    logging.info("Finished loading")
    return X, y

def get_model(X, y):
    model = sklearn.ensemble.RandomForestRegressor(
        n_estimators=0, warm_start=True, n_jobs=-1)
    indices = list(range(0, X.shape[0], CHUNKSIZE))
    indices.append(X.shape[0])
    for i in range(len(indices) - 1):
        if not (i + 1) % 10:
            logging.info("Fitting {} of {}".format(i + 1, len(indices) - 1))
        start, end = indices[i], indices[i + 1]
        model.set_params(n_estimators=model.get_params()["n_estimators"] + 1)
        model.fit(X[start: end], y[start: end])
    logging.info("Finished Training")
    return model

def get_index_and_features(path):
    imgarray = skimage.data.imread(str(path),as_grey=True)
    X = get_features_for_image(imgarray)
    index = []
    for i in range(imgarray.shape[0]):
        for j in range(imgarray.shape[1]):
            index.append("{}_{}_{}".format(path.stem, i + 1, j + 1))
    return index, X

def get_test_set():
    index = []
    X = []
    for imgindex, imgfeatures in joblib.Parallel(n_jobs=-1)(
            joblib.delayed(get_index_and_features)(i)
            for i in TEST_DIR.iterdir()):
        index.extend(imgindex)
        X.append(imgfeatures)
    logging.info("Finished Loading Test Set")
    X = np.vstack(X)
    assert(len(index) == X.shape[0])
    return index, X


def write_submission(model, index, X, path):
	print 'Writing Submission'
	mod=zip(model.predict(X))
	with open('rand_real.csv', 'w') as f:
		f.write("id,value\n")
		for x in xrange(len(index)):
			f.write("%s,%s\n"%(str(index[x]),str(mod[x][0])))
	return index,mod		
	'''
	with open("rand.csv","w") as f:
		f.write("id,value\n")
		for x in xrange(len(index)):
			f.write("%s,%s\n"%(str(index[x]),str(mod[x])))
	#print zip(index, model.predict(X))
	
    with path.open('wb', encoding='utf-8', newline='') as outf:
        writer = csv.writer(outf)
        writer.writerow(('id', 'value'))
        writer.writerows(zip(index, model.predict(X)))
    '''
if __name__ == "__main__":
    #trainX, trainy = get_training_sets()
    #model = get_model(trainX, trainy)
    #pickle.dump(model,open("model_rand.p","wb"))
    model1 = pickle.load(open("model_rand.p","rb"))
    index, testX = get_test_set()
    ind,mod=write_submission(model1, index, testX, Path("submission.csv"))
