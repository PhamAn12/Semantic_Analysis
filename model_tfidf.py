from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from polyglot.text import Text, Word
from readData import DataSource
from pyvi import ViTokenizer, ViPosTagger, ViUtils
from ultil import Pre_Process
from sklearn.svm import SVC
from underthesea import word_tokenize, pos_tag
import string
import re
from preprocess import util
from sklearn.metrics import accuracy_score
from langdetect import detect
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from translate import translator
import os


def identity_tokenizer(text):
    return text


def get_stop_word():
    stop_word = []
    with open("stop_word.txt", encoding="utf-8") as f:
        lines = f.readlines()
        for word in lines:
            if word.endswith('\n'):
                word = word[:-1]
            stop_word.append(word)
        f.close()
    return stop_word + list(string.punctuation)


class Dict_Data():

    def create_dict_tfidf(self):
        translator = str.maketrans('', '', string.punctuation)
        regexp = re.compile(
            r'[ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ]')
        tokenized_list_of_sentences = []
        # Load train_data_vi len
        ult, y_train = Pre_Process()
        # ult = ult[0:8]
        # y_train = y_train[0:8]
        count = 0
        arr_count = []
        stop_word = get_stop_word()
        Util = util()
        for data in ult:
            str_data = str(data)
            count = count + 1

            str_data = Util.text_util_final(str_data)

            if regexp.search(str_data):
                token = word_tokenize(str_data)
                new_token = []
                for t in token:
                    t = str(t)
                    if t.startswith('. '):
                        t = t.replace('. ', '')
                    t = t.lower()
                    if t not in stop_word:
                        new_token.append(t)
                # print(new_token)
                # count = count + 1
                print(count)
                tokenized_list_of_sentences.append(new_token)
            else:
                count = count + 1
                # print(count)
                arr_count.append(count)
                try:
                    token = word_tokenize(ViUtils.add_accents(str_data))
                except Exception:
                    pass

                new_token = []
                for t in token:
                    t = str(t)
                    if t.startswith('. '):
                        t = t.replace('. ', '')
                    t = t.lower()
                    if t not in stop_word:
                        new_token.append(t)
                #print(new_token)
                # arr_count.append(count)

                tokenized_list_of_sentences.append(new_token)

        # print(tokenized_list_of_sentences)

        vectorizer = TfidfVectorizer(tokenizer=identity_tokenizer, lowercase=False)
        # print(tokenized_list_of_sentences)
        vectorizer.fit(tokenized_list_of_sentences)
        X = vectorizer.transform(tokenized_list_of_sentences)

        model = SVC(C=1, kernel='linear', gamma='auto')
        model.fit(X, y_train)

        pre = []
        vector2 = []
        temp_arr = []
        # f = open("data/test_data", "r")
        f = open("data/main_data/test_data_final", "r")
        stop_word = get_stop_word()
        if f.mode == "r":
            lines = f.readlines()
            # lines = lines[0:5]
            for line in lines:
                # line = line.lower()
                # line = line.translate(translator)
                line = Util.text_util_final(line)
                if line.endswith('Tuyệt hảo\n') or line.endswith('Xuất sắc\n'):
                    pre.append(np.array(["__label__xuat_sac"]))
                elif line.endswith('Tốt\n') or line.endswith('tốt\n') or line.endswith('Tuyệt vời\n') or line.endswith(
                        'Rất tốt\n'):
                    pre.append(np.array(["__label__tot"]))
                elif line.endswith('Tàm tạm\n') or line.endswith('Dễ chịu\n') or line.endswith('Chấp nhận được\n'):
                    pre.append(np.array(["__label__trung_binh"]))
                elif line.endswith('Thất vọng\n') or line.endswith('Kém\n'):
                    pre.append(np.array(["__label__kem"]))
                elif line.endswith('Rất tệ\n'):
                    pre.append(np.array(["__label__rat_kem"]))
                else:
                    if regexp.search(line):
                        token = word_tokenize(line)
                        new_token = []
                        for t in token:
                            t = str(t)
                            t = t.lower()
                            if t.startswith('. '):
                                t = t.replace('. ', '')
                            if t not in stop_word:
                                new_token.append(t)
                        vector2 = vectorizer.transform([new_token])
                        # temp_arr.append(new_token)
                        pre.append(model.predict(vector2))
                    else:
                        try:
                            token = word_tokenize(ViUtils.add_accents(line))
                        except Exception:
                            pass

                        # count = count + 1
                        new_token = []
                        for t in token:
                            t = str(t)
                            t = t.lower()
                            if t.startswith('. '):
                                t = t.replace('. ', '')
                            if t not in stop_word:
                                new_token.append(t)
                        print(new_token)
                        # temp_arr.append(new_token)
                        vector2 = vectorizer.transform([new_token])
                        pre.append(model.predict(vector2))
                #print(token)

        f.close()
        # print(temp_arr)

        # vector2 = vectorizer.transform(temp_arr)
        # pre = model.predict(vector2)
        print(vector2.shape)
        # print(pre)
        return pre


if __name__ == '__main__':
    DD = Dict_Data()
    ds = DataSource()
    pre = DD.create_dict_tfidf()
    # print(get_stop_word())
    # print(DD.create_dict_tfidf().size)
    np_X_train, np_X_test, np_y_train, np_y_test = ds.train_test_split()

    X_train = np_X_train.tolist()
    X_train = X_train[0:100]
    y_test = np_y_test.tolist()
    # y_test = y_test[0:5]
    X_test = np_X_test.tolist()
    X_test = X_test[0:100]

    # print(y_test)
    # print(pre)

    print(classification_report(pre, y_test))
    print('accuracy = ', accuracy_score(y_test, pre))
