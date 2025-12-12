"""
heapq - 小根堆（也可以大根）

注:
  python 3.14 引入了 _max 等方法，可以支持大根堆
"""

from heapq import heappop, heappush


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def priority_queue(tasks):
    h = []
    for value in tasks:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def main():
    print(heapsort([4, 0, 0, 8]))  # [0, 0, 4, 8] 默认小根堆

    print(priority_queue([(5, "code"), (7, "release"), (1, "doc")]))
    # [(1, 'doc'), (5, 'code'), (7, 'release')]
    # 内部用 `<` 比较


main()
