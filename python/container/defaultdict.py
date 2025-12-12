"""
defaultdict: 带默认值的dict
"""

from collections import defaultdict


def main():
    di = defaultdict(int)
    di["a"] += 1
    print(di["a"])  # 1

    dlist = defaultdict(list)
    s = [("yellow", 1), ("blue", 2), ("yellow", 3)]
    for k, v in s:
        dlist[k].append(v)
    sort = sorted(dlist.items())
    print(sort)  # [("blue", [2]), ("yellow", [1, 3])]


main()
