import sys
import scipy
import numpy
import matplotlib
import sklearn
from loadGitData import *


#load data and return dataset
loadDataML = LoadDataML()
dataset = loadDataML.loadgitdata()
print(dataset.shape)
print(dataset.head(170))
print(dataset.describe())
print(dataset.groupby('user-comments').size())
