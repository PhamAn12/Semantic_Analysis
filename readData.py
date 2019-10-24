import numpy as np


class DataSource(object):

    def loadData(self, label):

        f = open("data/data_train.txt", "r")
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
