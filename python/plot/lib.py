import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def display_line(data):
    """折线图"""
    data = np.array(data)
    plt.figure()  # 清除
    plt.plot(data)
    plt.show()


def display_bar(titles, values):
    """柱状图"""
    categories = titles
    values = values

    plt.figure()  # 清除
    plt.bar(categories, values, color="skyblue")
    plt.title("Basic Bar Chart")
    plt.show()


def display_scatter(points):
    """散点图"""
    points = np.array(points, dtype=float)
    x, y = points[:, 0], points[:, 1]
    colors = np.random.randn(len(points))
    area = np.full(len(points), 200.0)

    plt.figure()  # 清除
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap="viridis")
    plt.title("Bubble Scatter Plot")

    plt.tight_layout()
    plt.show()


def display_map(data):
    """
    给定一个二维数组，用 plot 显示出来，0 = 白色，1 = 蓝色, 2...
    """
    data = np.array(data)
    max_val = int(np.max(data))
    rows, cols = data.shape
    colors = ["white", "blue", "green", "orange", "red", "purple", "brown"]
    cmap = ListedColormap(colors[: max_val + 1])

    plt.figure()
    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap)
    ax.set_xticks(np.arange(cols))
    ax.set_yticks(np.arange(rows))
    plt.show()


def display_segment(segments):
    # 定义线段的数据：[(x1, y1), (x2, y2)]
    points = []
    for index, seg in enumerate(segments):
        points.append([[seg[0], index * 0.5], [seg[1], index * 0.5]])

    plt.figure(figsize=(6, 6))

    for i, seg in enumerate(points):
        # 解包坐标：x_coords = [start_x, end_x], y_coords = [start_y, end_y]
        x_coords = [seg[0][0], seg[1][0]]
        y_coords = [seg[0][1], seg[1][1]]

        # 绘制线段，marker='o' 可以标出端点
        plt.plot(x_coords, y_coords, marker="o", label=f"Segment {i + 1}")

    plt.title("Visualizing Line Segments")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()


def display_hist(data, bins=20):
    """分布直方图"""
    plt.figure()
    plt.hist(data, bins=bins, color="teal", edgecolor="white", alpha=0.7)
    plt.axvline(
        np.mean(data), color="red", linestyle="dashed", label="Mean"
    )  # 标出平均值线
    plt.title("Data Distribution")
    plt.legend()
    plt.show()


def display_box(data_list, labels=None):
    """箱线图（支持多组数据对比）"""
    plt.figure()
    plt.boxplot(
        data_list,
        labels=labels,
        patch_artist=True,
        boxprops=dict(facecolor="lightblue"),
    )
    plt.title("Statistical Summary")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
