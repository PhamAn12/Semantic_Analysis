import numpy as np
from readData import DataSource
from textblob import TextBlob
from langdetect import detect


def classify_lang(label):
    ds = DataSource()
    tot = ds.loadData(label)
    array_vi = []
    for text in tot:
        lang = detect(text)
        if lang == "vi":
            array_vi.append(text)
    np_array_vi = np.array(array_vi)
    print(np_array_vi.size)
    return np_array_vi


def create_vi_file(name_file, label):
    f = open(name_file, "w+")
    np_temp_array = classify_lang(label)
    for line in np_temp_array:
        f.write(line)
    f.close()


if __name__ == '__main__':
    create_vi_file("xuat_sac_vi", "__label__xuat_sac")
