'''
Created on Dec 31, 2016

@author: dexter
'''

from nltk.metrics import masi_distance
from nltk.metrics import jaccard_distance 
import nltk
class Sentence:
    '''
    a class for sentence analysis
    '''

    def __init__(self, mystr):
        '''
        Constructor
        '''
        self.mystr=mystr
        self.tokenized=False
    
    def init(self):
        if(not self.tokenized):
            myToken= nltk.word_tokenize(self.mystr)
            self.myToken=set(myToken)
    
    def calculateJaccardDist(self, otherSentence):
        self.init()
        otherSentence.init()
        return jaccard_distance(self.myToken,otherSentence.myToken)
    def calculateMasiDist(self, otherSentence):
        self.init()
        otherSentence.init()
        return masi_distance(self.myToken,otherSentence.myToken)