"""
python 自带了 bisect_left 、bisect_right 函数

bisect_left(a, x, lo=0, hi=len(a), *, key=None)
目标是找到一个插入点，使得插入元素 x 后，列表依然保持有序
bisect_right(a, x, lo=0, hi=len(a), *, key=None)
"""

import bisect


def main():
    nums = [1, 3, 3, 3, 5, 7, 9]

    # >= x 的第一个元素的下标: bisect_left(nums, x)，不存在则为 n
    print(bisect.bisect_left(nums, 1))  # 0
    print(bisect.bisect_left(nums, 2))  # 1
    print(bisect.bisect_left(nums, 0.5))  # 0
    print(bisect.bisect_left(nums, 100))  # 7

    # > x 的第一个元素的下标: bisect_right(nums, x)，不存在则为 n
    print('----------')
    print(bisect.bisect_right(nums, 1))  # 1
    print(bisect.bisect_right(nums, 2))  # 1
    print(bisect.bisect_right(nums, 3))  # 4
    print(bisect.bisect_right(nums, 0.5))  # 0
    print(bisect.bisect_right(nums, 100))  # 7

    # < x 的最后一个元素的下标: bisect_left(nums, x) - 1，不存在则为 -1
    print('----------')
    print(bisect.bisect_left(nums, 1) - 1)  # -1
    print(bisect.bisect_left(nums, 2) - 1)  # 0
    print(bisect.bisect_left(nums, 3) - 1)  # 0
    print(bisect.bisect_left(nums, 0.5) - 1)  # -1
    print(bisect.bisect_left(nums, 100) - 1)  # 6

    # <= x 的最后一个元素的下标: bisect_right(nums, x) - 1，不存在则为 -1
    print('----------')
    print(bisect.bisect_right(nums, 1) - 1)  # 0
    print(bisect.bisect_right(nums, 2) - 1)  # 0
    print(bisect.bisect_right(nums, 3) - 1)  # 3
    print(bisect.bisect_right(nums, 0.5) - 1)  # -1
    print(bisect.bisect_right(nums, 100) - 1)  # 6


main()
