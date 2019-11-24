from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, make_scorer, f1_score
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
from sklearn.model_selection import train_test_split, GridSearchCV
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
        # ult = ult[0:6]
        # y_train = y_train[0:6]
        count = 0
        arr_count = []
        stop_word = get_stop_word()
        Util = util()
        for data in ult:
            str_data = str(data)
            # count = count + 1

            str_dataa = Util.text_util_final(str_data)
            # print(str_dataa)
            if regexp.search(str_dataa):
                token = word_tokenize(str_dataa)
                new_token = []
                for t in token:
                    t = str(t)
                    if t.startswith('. '):
                        t = t.replace('. ', '')
                    t = t.lower()
                    if t not in stop_word:
                        new_token.append(t)
                print(new_token)
                # count = count + 1
                # print(count)
                tokenized_list_of_sentences.append(new_token)
            else:
                count = count + 1
                # print(count)
                arr_count.append(count)
                try:
                    token = word_tokenize(ViUtils.add_accents(str_dataa))
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
                print(new_token)
                # arr_count.append(count)

                tokenized_list_of_sentences.append(new_token)

        print(tokenized_list_of_sentences)

        vectorizer = TfidfVectorizer(min_df=2, max_df=0.9, tokenizer=identity_tokenizer, lowercase=False,
                                     ngram_range=(1, 2))
        # print(tokenized_list_of_sentences)
        vectorizer.fit(tokenized_list_of_sentences)
        X = vectorizer.transform(tokenized_list_of_sentences)

        model = SVC(C=1, kernel='linear', gamma='auto')
        model.fit(X, y_train)
        # parameter_candidates = [
        #     {'C': [0.1, 1, 2, 3, 4, 5], 'kernel': ['linear']},
        #     {'C': [0.1, 1, 2, 3, 4, 5], 'kernel': ['rbf'], 'gamma': [0.01, 0.05]}
        # ]
        # my_scorer = make_scorer(f1_score, greater_is_better=True, average='micro')
        # clf = GridSearchCV(estimator=SVC(), param_grid=parameter_candidates, scoring=my_scorer)
        # print("mode istraining....")
        # clf.fit(X, y_train)
        # print('Best score:', clf.best_score_)
        # print("Best parameter_gram:", clf.best_params_)
        pre = []
        vector2 = []
        temp_arr = []
        # f = open("data/test_data", "r")
        # f = open("data/main_data/test_data_vi_final_1", "r")
        f = open("data/main_data/test_data_final_1","r")
        stop_word = get_stop_word()
        if f.mode == "r":
            lines = f.readlines()
            # lines = lines[0:5]
            for line in lines:
                # line = line.lower()
                # line = line.translate(translator)
                linee = Util.text_util_final(line)
                if linee.endswith('Tuyệt hảo\n') or linee.endswith('Xuất sắc\n') or linee.endswith('Tuyệt hảo') or linee.endswith('Xuất sắc'):
                    pre.append(np.array(["__label__xuat_sac"]))
                elif linee.endswith('Tốt\n') or linee.endswith('Tuyệt vời\n') or linee.endswith(
                        'Rất tốt\n') or linee.endswith('Tốt') or linee.endswith('Tuyệt vời') or linee.endswith(
                        'Rất tốt'):
                    pre.append(np.array(["__label__tot"]))
                elif linee.endswith('Tàm tạm\n') or linee.endswith('Dễ chịu\n') \
                        or linee.endswith('Chấp nhận được\n') or linee.endswith('Tàm tạm') or linee.endswith('Dễ chịu') or linee.endswith('Chấp nhận được'):
                    pre.append(np.array(["__label__trung_binh"]))
                elif linee.endswith('Thất vọng\n') or linee.endswith('Kém\n') or linee.endswith('Thất vọng') or linee.endswith('Kém'):
                    pre.append(np.array(["__label__kem"]))
                elif linee.endswith('Rất tệ\n') or linee.endswith('Rất tệ'):
                    pre.append(np.array(["__label__rat_kem"]))
                else:
                    if regexp.search(linee):
                        token = word_tokenize(linee)
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
                            token = word_tokenize(ViUtils.add_accents(linee))
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
                # print(token)

        f.close()
        print(temp_arr)

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
    # print(str(pre[0]))
    # pre_list = pre[0:10]
    # print(type(pre_list))
    # for i in pre[0:10]:
    #     print(type(str(i[0])))
    # f_train = open("sentiment_analysis_team11_solution22.result.txt", "w+")
    # for i in pre:
    #     f_train.write(str(i[0]) + "\n")
    # f_train.close()

    print(classification_report(pre, y_test))
    print('accuracy = ', accuracy_score(y_test, pre))
