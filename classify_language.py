import numpy as np
from readData import DataSource
from textblob import TextBlob
from langdetect import detect


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
    f_train = open("train_data", "w+")
    for i in range(X_train.size):
        f_train.write(y_train[i] + X_train[i])
    f_train.close()

    f_test = open("test_data", "w+")
    for i in range(X_test.size):
        f_test.write(X_test[i])
    f_test.close()


if __name__ == '__main__':
    create_train_test_file()
    # create_vi_file("rat_kem_non_vi", "__label__rat_kem")
    # create_vi_file("kem_non_vi", "__label__kem")
    # create_vi_file("tot_non_vi", "__label__tot")
    # create_vi_file("trung_binh_non_vi", "__label__trung_binh")
    # create_vi_file("xuat_sac_non_vi", "__label__xuat_sac")
