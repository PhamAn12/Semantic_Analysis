# - *- coding: utf- 8 - *-
import numpy as np
from readData import DataSource
# from textblob import TextBlob
from langdetect import detect
from googletrans import Translator


def classify_lang(label):
    ds = DataSource()
    tot = ds.loadData(label)
    translator = Translator()
    raw_data = np.char.strip(tot, chars=label)
    array_vi = []
    for text in raw_data:
        dete = translator.detect(text)
        print text
        # lang = detect(text)
        if dete.lang == "vi" and dete.confidence == 1:
            array_vi.append(text)
        else:
            # - *- coding: utf- 8 - *-
            newText = translator.translate(text, dest='vi').text
            newnew = newText.encode("utf8")
            array_vi.append(newnew)
    np_array_vi = np.array(array_vi)
    return np_array_vi


def create_vi_file(name_file, label):
    f = open(name_file, "w+")
    np_temp_array = classify_lang(label)
    for line in np_temp_array:
        f.write((label+ " " +line + "\n"))
    f.close()


if __name__ == '__main__':
    create_vi_file("rat_kem_non_vi", "__label__rat_kem")
    create_vi_file("kem_non_vi", "__label__kem")
    create_vi_file("tot_non_vi", "__label__tot")
    create_vi_file("trung_binh_non_vi", "__label__trung_binh")
    create_vi_file("xuat_sac_non_vi", "__label__xuat_sac")
