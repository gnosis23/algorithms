"""
python 标准库提供了双向队列 deque
- 左右两侧插入和弹出复杂度为 O(1)
"""

from collections import deque


def main():
    d = deque()

    d.append("a")
    d.appendleft("l")
    d.append("b")

    print(d)
    # deque('l', 'a', 'b')

    while d:
        t = d.popleft()
        print(t)


main()
