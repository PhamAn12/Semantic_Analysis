import matplotlib.pyplot as plt
from readData import DataSource


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


if __name__ == '__main__':
    visualize()
