from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from readData import DataSource
from pyvi import ViTokenizer, ViPosTagger, ViUtils
from translate import translator
import os


class Dict_Data():
    def create_dict_tfidf(self):
        ds = DataSource()
        A = ds.load_file("data/vi/rat_kem_vi").tolist()
        A = np.char.strip(A, chars="__label__rat_kem ")
        B = []
        dict_data = A[0:10]
        for data in dict_data:
            a = data.lower()

            text_token = ViTokenizer.tokenize(a)
            B.append(text_token)
        #print(B)

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(B)
        #print(vectorizer.get_feature_names())
        #print(X)

        XX = translator('zh-TW','vi',"态度很不好 . Rất tệ")
        print(XX)

if __name__ == '__main__':
    DD = Dict_Data()
    DD.create_dict_tfidf()
