import numpy as np
from sklearn.model_selection import train_test_split


class DataSource(object):
    def train_test_split(self):

        global raw_data, label_data
        f = open("data/main_data/final_data", "r")
        if f.mode == "r":
            lines = f.readlines()
            raw_data = []
            label_data = []
            for line in lines:
                if line.startswith("__label__kem"):
                    raw_data.append(line[12:])
                    label_data.append(line[:12])
                elif line.startswith("__label__rat_kem"):
                    raw_data.append(line[16:])
                    label_data.append(line[:16])
                elif line.startswith("__label__tot"):
                    raw_data.append(line[12:])
                    label_data.append(line[:12])
                elif line.startswith("__label__trung_binh"):
                    raw_data.append(line[19:])
                    label_data.append(line[:19])
                elif line.startswith("__label__xuat_sac"):
                    raw_data.append(line[17:])
                    label_data.append(line[:17])
        X_train, X_test, y_train, y_test = train_test_split(raw_data, label_data, test_size=0.2, random_state=42)
        np_X_train = np.array(X_train)
        np_X_test = np.array(X_test)
        np_y_train = np.array(y_train)
        np_y_test = np.array(y_test)
        return np_X_train,np_X_test,np_y_train,np_y_test

    def loadData(self, label):

        f = open("data/data_thay.txt", "r")
        if f.mode == "r":

            lines = f.readlines()
            arrayLabel = []
            for line in lines:

                if line.startswith(label):
                    arrayLabel.append(line)
        mat = np.array(arrayLabel)
        return mat

    def load_file(self, path):
        f = open(path, "r")
        if f.mode == "r":
            lines = f.readlines()
            arr_data = []
            for line in lines:
                arr_data.append(line)
        np_arr_data = np.array(arr_data)
        return np_arr_data
