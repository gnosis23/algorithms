"""
Python 提供了方便的计数器
"""

from collections import Counter


def main():
    cnt = Counter()

    for word in ["red", "blue", "red", "green", "blue", "blue"]:
        cnt[word] += 1

    print(cnt["red"])  # 2
    print(cnt["blue"])  # 3
    print(cnt["orange"])  # 0, 不存在默认为0


main()
