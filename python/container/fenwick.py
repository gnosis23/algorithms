"""
树状数组: 统计前n个元素和
元素储存在 [1, n]
"""


class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.data = [0] * (n + 1)

    def sum(self, i: int) -> int:
        """
        统计 [0, i] 元素的和
        i 范围 [0, n)
        """
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
        """
        为索引 i 的元素**增加a**
        i 范围 [0, n)
        """
        n = i + 1
        while n <= self.n:
            self.data[n] += a
            n += n & -n
