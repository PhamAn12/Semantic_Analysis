import numpy as np
from readData import DataSource
from textblob import TextBlob
from langdetect import detect
from mtranslate import translate


def classify_lang(label):
    ds = DataSource()
    tot = ds.loadData(label)
    raw_data = np.char.strip(tot, chars=label)
    array_vi = []
    for text in raw_data:
        lang = detect(text)
        if lang != "vi":
            array_vi.append(text)
    np_array_vi = np.array(array_vi)
    print(np_array_vi.size)
    return np_array_vi


def create_vi_file(name_file, label):
    f = open(name_file, "w+")
    np_temp_array = classify_lang(label)
    for line in np_temp_array:
        f.write(label + line)
    f.close()


def create_train_test_file():
    ds = DataSource()
    X_train, X_test, y_train, y_test = ds.train_test_split()
    print(X_train.size)
    print(y_train.size)
    print(X_test.size)
    f_train = open("train_data_final_1", "w+")
    for i in range(X_train.size):
        f_train.write(y_train[i] + X_train[i])
    f_train.close()

    f_test = open("test_data_final_1", "w+")
    for i in range(X_test.size):
        f_test.write(X_test[i])
    f_test.close()


def translate_file(path):
    arr_end_word = ['Chấp nhận được', 'Rất tốt', 'Tuyệt vời', 'Xuất sắc', 'Tốt', 'Tuyệt hảo',
                 'Tàm tạm','Dễ chịu', 'Dễ chịu', 'Thất vọng','Kém']
    ds = DataSource()
    arr = ds.load_file(path)
    # arr = arr[0:100]
    f_train = open("test_data_vi_final_2", "w+")
    for l in arr:
        lines = str(l)
        line = lines.strip()
        if detect(line) != "vi":
            str_line = str(line)
            # print(str_line)
            flag = 1
            for end_word in arr_end_word:
                if str_line.endswith(end_word):
                    flag = 0
                    leng_word = len(end_word)
                    str_line = str_line[:-leng_word]
                    data = translate(str_line, "vi", "auto")
                    print(data + end_word)
                    f_train.write(data + end_word)
                    break
            if flag == 1:
                print(translate(str_line, "vi", "auto"))
                f_train.write(translate(str_line, "vi", "auto")+ '\n')
        else:
            f_train.write(line)
    f_train.close()


if __name__ == '__main__':
    # create_train_test_file()
    translate_file('data/main_data/sentiment_analysis_test.txt')
    # create_vi_file("rat_kem_non_vi", "__label__rat_kem")
    # create_vi_file("kem_non_vi", "__label__kem")
    # create_vi_file("tot_non_vi", "__label__tot")
    # create_vi_file("trung_binh_non_vi", "__label__trung_binh")
    # create_vi_file("xuat_sac_non_vi", "__label__xuat_sac")
