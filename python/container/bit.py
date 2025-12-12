"""
树状数组: 统计前n个元素和
元素储存在 [1, n]
"""


class BinaryIndexedTree:
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

    def add(self, i: int, a: int) -> None:
        """
        为索引 i 的元素**增加a**
        i 范围 [0, n)
        """
        n = i + 1
        while n <= self.n:
            self.data[n] += a
            n += n & -n


def main():
    bit = BinaryIndexedTree(5)
    bit.add(0, 5)
    bit.add(1, 3)
    bit.add(2, 7)
    bit.add(3, 2)
    bit.add(4, 8)

    print(bit.sum(0))  # 5
    print(bit.sum(1))  # 8
    print(bit.sum(2))  # 15
    print(bit.sum(3))  # 17
    print(bit.sum(4))  # 25

    # update 0
    bit.add(0, -1)

    print(bit.sum(0))  # 4
    print(bit.sum(1))  # 7
    print(bit.sum(2))  # 14


main()
