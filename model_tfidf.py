from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from readData import DataSource
from textblob import TextBlob
from langdetect import detect


class Dict_Data():
    def create_dict_tfidf(self):
        ds = DataSource()
        A = ds.loadData("__label__rat_kem").tolist()
        dict_data = A[0:9]
        # dict_data = dict_data.tolist()
        # instantiate CountVectorizer()
        # print(dict_data_rat_kem)
        cv = CountVectorizer()

        # this steps generates word counts for the words in your docs
        word_count_vector = cv.fit_transform(dict_data)
        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        tfidf_transformer.fit(word_count_vector)
        # print idf values
        df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(), columns=["idf_weights"])

        # sort ascending
        df_idf.sort_values(by=['idf_weights'])
        # print(df_idf)
        # for text in dict_data:
        # b = TextBlob("text")
        lang = detect("房间Wi-Fi不稳定！ 非常完美的小酒店，超级喜欢！躺在游泳池边吹着海风无比惬意！服务非常周到！ . Xuất sắc")
        print (lang)


if __name__ == '__main__':
    DD = Dict_Data()
    DD.create_dict_tfidf()