# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:03:11 2022

@author: samay
"""

import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer



def clean(query):
        new_review = query
        new_review = re.sub('[^a-zA-Z]', ' ', new_review)
        new_review = new_review.lower() 
        new_review = new_review.split()
        ps = PorterStemmer()
        new_review = [ps.stem(word) for word in new_review]
        new_review = ' '.join(new_review)
        new_corpus = [new_review]
        corpus = ' '.join([str(elem) for elem in new_corpus])        
        print(corpus)
        return corpus
    

