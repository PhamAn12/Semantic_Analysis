from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from readData import DataSource
from pyvi import ViTokenizer, ViPosTagger, ViUtils
from ultil import Pre_Process
from sklearn.model_selection import train_test_split
from translate import translator
import os


class Dict_Data():
    def create_dict_tfidf(self):
        ult = Pre_Process().tolist()
        vi_word_arr = []
        for data in ult:
            str_data = str(data)
            str_data.lower()
            text_token = ViTokenizer.tokenize(str_data)
            vi_word_arr.append(text_token)
        print(vi_word_arr[0])

        vectorizer = TfidfVectorizer()
        tfidf_vector = vectorizer.fit_transform(vi_word_arr)
        first_vector = tfidf_vector[0]
        df = pd.DataFrame(first_vector.T.todense(),index=vectorizer.get_feature_names(), columns=["tfidf"])

        print(first_vector)
        print(df)
        return tfidf_vector


if __name__ == '__main__':
    DD = Dict_Data()
    DD.create_dict_tfidf()
