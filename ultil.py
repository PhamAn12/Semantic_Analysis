# - *- coding: utf- 8 - *-
from readData import DataSource
import numpy as np
from googletrans import Translator
from langdetect import detect
from mtranslate import translate
import time

def Pre_Process():
    ds = DataSource()
    count = 1
    # train_data = ds.load_file("data/data_thay.txt")
    train_data = ds.load_file("data/main_data/train_data_final")
    translator = Translator()
    # train_data = train_data[0:100]
    train_raw_data = []
    y_train = []
    for data in train_data:
        str_data = str(data)

        if str_data.startswith("__label__tot"):
            # Handle_Data(str_data, train_raw_data, "__label__tot",y_train)
            Handle_Data_1(str_data, train_raw_data, "__label__tot", y_train)
            # str_data = str_data[13:]
            # dete = translator.detect(str_data)
            # if dete.lang == "vi" and dete.confidence == 1:
            #     train_raw_data.append(str_data)
            #     y_train.append(str_data[:13])
            # else:
            #     # - *- coding: utf- 8 - *-
            #     newText = translator.translate(str_data, dest='vi').text
            #     print(newText)
            #     train_raw_data.append(newText)
            #     y_train.append(str_data[:13])
        elif str_data.startswith("__label__xuat_sac"):
            # Handle_Data(str_data, train_raw_data, "__label__xuat_sac",y_train)
            Handle_Data_1(str_data, train_raw_data, "__label__xuat_sac", y_train)
            # str_data = str_data[18:]
            # dete = translator.detect(str_data)
            # if dete.lang == "vi" and dete.confidence == 1:
            #     train_raw_data.append(str_data)
            #
            # else:
            #     # - *- coding: utf- 8 - *-
            #     newText = translator.translate(str_data, dest='vi').text
            #     print(newText)
            #     train_raw_data.append(newText)
        elif str_data.startswith("__label__trung_binh"):
            # Handle_Data(str_data, train_raw_data, "__label__trung_binh",y_train)
            Handle_Data_1(str_data, train_raw_data, "__label__trung_binh", y_train)
            # str_data = str_data[20:]
            # dete = translator.detect(str_data)
            # if dete.lang == "vi" and dete.confidence == 1:
            #     train_raw_data.append(str_data)
            # else:
            #     # - *- coding: utf- 8 - *-
            #     newText = translator.translate(str_data, dest='vi').text
            #     print(newText)
            #     train_raw_data.append(newText)
        elif str_data.startswith("__label__kem"):
            # Handle_Data(str_data, train_raw_data, "__label__kem",y_train)
            Handle_Data_1(str_data, train_raw_data, "__label__kem", y_train)
            # str_data = str_data[13:]
            # dete = translator.detect(str_data)
            # if dete.lang == "vi" and dete.confidence == 1:
            #     train_raw_data.append(str_data)
            # else:
            #     # - *- coding: utf- 8 - *-
            #     newText = translator.translate(str_data, dest='vi').text
            #     print(newText)
            #     train_raw_data.append(newText)
        elif str_data.startswith("__label__rat_kem"):
            # Handle_Data(str_data, train_raw_data, "__label__rat_kem",y_train)
            Handle_Data_1(str_data, train_raw_data, "__label__rat_kem", y_train)
            # str_data = str_data[17:]
            # dete = translator.detect(str_data)
            # if dete.lang == "vi" and dete.confidence == 1:
            #     train_raw_data.append(str_data)
            # else:
            #     # - *- coding: utf- 8 - *-
            #     newText = translator.translate(str_data, dest='vi').text
            #     print(newText)
            #     train_raw_data.append(newText)
    return np.array(train_raw_data), np.array(y_train)
# Doc file train_data_vi
def Handle_Data_1(str_data,train_raw_data,label,yy_train):
    length_label = len(label)
    str_dataa = str_data[length_label:]
    yy_train.append(label)
    train_raw_data.append(str_dataa)
# Dich file train_data
def Handle_Data(str_data, train_raw_data, label, yy_train):
    global data_vi
    arr_end_word = ['Chấp nhận được\n', 'Rất tốt\n', 'Tuyệt vời\n', 'Xuất sắc\n', 'Tuyệt hảo\n', 'Tốt\n', 'Tuyệt hảo',
                    'Xuất sắc', 'Tàm tạm\n','Dễ chịu\n', 'Dễ chịu', 'Thất vọng\n','Thất vọng','Kém\n','Kém']
    translator = Translator()
    length_label = len(label)
    str_dataa = str_data[length_label:]
    # label = str_data[:length_label]
    # print(str_dataa)
    yy_train.append(label)

    if detect(str_dataa) != 'vi':
        flag = 1
        for end_word in arr_end_word:
            if str_dataa.endswith(end_word):
                flag = 0
                leng_word = len(end_word)
                str_line = str_dataa[:-leng_word]
                data = translate(str_line, "vi", "auto")
                # print(data + end_word)
                data_vi = data + end_word
                train_raw_data.append(data_vi)
                break
        if flag == 1:
            # print(translate(str_dataa, "vi", "auto"))
            data_vi = translate(str_dataa, "vi", "auto")
            train_raw_data.append(data_vi + '\n')
    else:
        train_raw_data.append(str_dataa)
    # dete = translator.detect(str_dataa)
    # time.sleep(2)
    # if dete.lang == "vi" and dete.confidence == 1:
    #     train_raw_data.append(str_dataa)
    #
    # else:
    #     # - *- coding: utf- 8 - *-
    #     newText = translator.translate(str_dataa, dest='vi').text
    #     train_raw_data.append(newText)


if __name__ == '__main__':
    # pre_process()
    X_train, yyy_train = Pre_Process()

    # f_train = open("train_data_vi", "w+")
    f_train = open("data_thay_vi", "w+")
    for i in range(X_train.size):
        f_train.write(yyy_train[i] + X_train[i])
    f_train.close()
