"""
树状数组: 统计前n个元素和
i 范围 [0, n-1]
下标统一闭区间
"""


class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.data = [0] * (n + 1)

    def sum(self, i: int) -> int:
        n = i + 1
        total = 0
        while n:
            total += self.data[n]
            n = n & (n - 1)
        return total

    def range_sum(self, low: int, high: int) -> int:
        sumr = self.sum(high)
        suml = self.sum(low - 1) if low > 0 else 0
        return sumr - suml

    def add(self, i: int, a: int) -> None:
        n = i + 1
        while n <= self.n:
            self.data[n] += a
            n += n & -n
