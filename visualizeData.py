import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import lxml.html
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from underthesea import word_tokenize, pos_tag
from pyvi import ViUtils
import nltk
# nltk.download('punkt')
from readData import DataSource
from preprocess import util
import string
import re
from langdetect import detect
from aiogoogletrans import Translator
from mtranslate import translate
import polyglot
from polyglot.text import Text, Word
import asyncio


def visualize():
    ds = DataSource()
    tot = ds.loadData("__label__tot").size
    xuat_sac = ds.loadData("__label__xuat_sac").size
    kem = ds.loadData("__label__kem").size
    rat_kem = ds.loadData("__label__rat_kem").size
    trung_binh = ds.loadData("__label__trung_binh").size
    left = [1, 2, 3, 4, 5]
    height = [tot, xuat_sac, kem, rat_kem, trung_binh]

    # labels for bars
    tick_label = ['tot', 'xuat_sac', 'kem', 'rat_kem', 'trung_binh']

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['red', 'green'])
    plt.show()


def identity_tokenizer(text):
    return text


if __name__ == '__main__':
    # print(list(string.punctuation))
    # a = word_tokenize("Dịch vụ Tốt")
    # b = pos_tag('Chợ thịt chó nổi tiếng ở Sài Gòn, Hà Nội bị truy quét')
    # c = " nhiet tinh"
    #
    # print (ViUtils.add_accents(c))
    # r = '[òóọỏõôồốộổỗơờớợởỡ]'i
    # regexp = re.compile(r'[ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ]')
    # if regexp.search(c):
    #     print("matched")
    # text = 'fhsjkdfh*&^%???///:))jkdfhskdjfhf jfdfjd ) kd'
    # new_string = text.translate(text.maketrans(string.punctuation, '                                '))
    # pattern = re.compile(r'\s+')
    # new_string = re.sub(pattern, ' ', new_string)
    # print(new_string)

    f = open("data/main_data/sentiment_analysis_test.txt", "r")
    count = 0
    if f.mode == "r":
        lines = f.readlines()
        for line in lines:
            line = line.strip()

            if line.endswith('Tàm tạm\n') or line.endswith('Dễ chịu\n') \
                        or line.endswith('Chấp nhận được\n') or line.endswith('Tàm tạm') or line.endswith('Dễ chịu') or line.endswith('Chấp nhận được'):
                count = count + 1
                # print(count)
    print(count)
    # print(b)
