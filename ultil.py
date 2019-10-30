from readData import DataSource
import numpy as np


def Pre_Process():
    ds = DataSource()
    train_data = ds.load_file("data/train_data")
    train_data = train_data[2:4]
    train_raw_data = []
    for data in train_data:
        str_data = str(data)
        if str_data.startswith("__label__tot "):
            str_data = str_data[13:]
            train_raw_data.append(str_data)
        elif str_data.startswith("__label__xuat_sac "):
            str_data = str_data[18:]
            train_raw_data.append(str_data)
        elif str_data.startswith("__label__trung_binh "):
            str_data = str_data[20:]
            train_raw_data.append(str_data)
        elif str_data.startswith("__label__kem "):
            str_data = str_data[13:]
            train_raw_data.append(str_data)
        elif str_data.startswith("__label__rat_kem "):
            str_data = str_data[17:]
            train_raw_data.append(str_data)
    return np.array(train_raw_data)


if __name__ == '__main__':
    # pre_process()
    print(Pre_Process())
