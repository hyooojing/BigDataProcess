#!/usr/bin/python3
import numpy as np
from os import listdir
import operator
import sys

training = sys.argv[1]
test = sys.argv[2]

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1))-dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def vector(fname) :
    vect = np.zeros((1, 1024))
    f = open(fname)
    for i in range(32):
        str = f.readline()
        for j in range(32):
            vect[0, 32*i+j] = int(str[j])
    return vect

def knn(k):
    labels = []
    trainingList = listdir(training)
    length1 = len(trainingList)
    trainingMat = np.zeros((length1, 1024))

    for i in range(length1):
        fullName = trainingList[i]
        fileName = fullName.split('.')[0]
        classNum = int(fileName.split('_')[0])
        labels.append(classNum)
        trainingMat[i, :] = vector('%s/%s' % (training, fullName))

    testList = listdir(test)
    cnt = 0
    length2 = len(testList)
    for i in range(length2):
        fullName = testList[i]
        fileName = fullName.split('.')[0]
        classNum = int(fileName.split('_')[0])
        vectorUnderTest = vector('%s/%s' % (test, fullName))
        rslt = classify0(vectorUnderTest, trainingMat, labels, k)
        if rslt != classNum:
            cnt += 1
    print(int(cnt / length2 * 100))

if __name__ == "__main__":
	for i in range(1, 21):
    		knn(i)

