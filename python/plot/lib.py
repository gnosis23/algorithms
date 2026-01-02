import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def display_line(data):
    """折线图"""
    data = np.array(data)
    plt.plot(data)


def display_map(data):
    """
    给定一个二维数组，用 plot 显示出来，0 = 白色，1 = 蓝色
    """
    data = np.array(data)
    rows, cols = data.shape
    cmap = ListedColormap(["white", "#0098df"])
    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap)
    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    plt.show()
