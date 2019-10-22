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
