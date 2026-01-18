"""
python 自带了 bisect_left 、bisect_right 函数

bisect_left(a, x, lo=0, hi=len(a), *, key=None)
目标是找到一个插入点，使得插入元素 x 后，列表依然保持有序
bisect_right(a, x, lo=0, hi=len(a), *, key=None)
"""

import bisect


def find_right_lte(a: list[int], x: int) -> int:
    """
    返回最大的插入坐标使得a为顺序

    :param a: 非降序列表
    :param x: 目标值
    :return: 坐标，[0, n]
    """
    i = bisect.bisect_right(a, x)
    return i


def find_left_lte(a: list[int], x: int) -> int:
    """
    返回最小的插入坐标使得a为顺序
    practice: https://leetcode.cn/problems/search-insert-position

    :param a: 非降序列表
    :param x: 目标值
    :return: 坐标，[0, n]
    """
    i = bisect.bisect_left(a, x)
    return i


def main():
    lst = [1, 3, 3, 3, 5, 7, 9]

    # [1, 3, 3, 3, 5, 7, 9]
    #  l
    #  r
    print(find_left_lte(lst, 0))  # 0
    print(find_right_lte(lst, 0))  # 0

    # [1, 3, 3, 3, 5, 7, 9]
    #  l
    #     r
    print(find_left_lte(lst, 1))  # 0
    print(find_right_lte(lst, 1))  # 1

    # [1, 3, 3, 3, 5, 7, 9]
    #     l
    #              r
    print(find_left_lte(lst, 3))  # 1
    print(find_right_lte(lst, 3))  # 4

    # [1, 3, 3, 3, 5, 7, 9]
    #              l
    #                 r
    print(find_left_lte(lst, 5))  # 4
    print(find_right_lte(lst, 5))  # 5

    # [1, 3, 3, 3, 5, 7, 9]
    #                       l
    #                       r
    print(find_left_lte(lst, 10))  # 7
    print(find_right_lte(lst, 10))  # 7

    # 搜索部分元素
    nums = [0, 1, 4, 5, 6]
    print(bisect.bisect_left(range(3), 4, key=lambda x: nums[x]))  # 2
    print(bisect.bisect_left(range(3), 0, key=lambda x: nums[x]))  # 0
    print(bisect.bisect_left(range(3), 2, key=lambda x: nums[x]))  # 1


main()
