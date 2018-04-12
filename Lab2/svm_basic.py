from classifier import classifier
from svmMLIA import smoPK,calcWs
import numpy as np
from numpy import *
from time import sleep


class SVM(classifier):

    def __init__(self):
        self.b = None
        self.alphas = None
        self.w = None
        
    def fit(self, X, Y):
        self.b, self.alphas = smoPK(X, Y,0.6, 0.001, 40)
        self.w = calcWs(self.alphas,X,Y)
        return self.w, self.b
 
    def predict(self, X):
        predict = np.sign(np.dot(np.array(X),self.w)+self.b)
        return predict.astype(int)
        # sign( x.w^T+b )