"""
线段树
区间为[0, n)，左闭右开

参数解释：
- op: 二元运算符，必须满足结合律。如加法、乘法、最大值、最小值、位运算等等
- e: 单位元。对于 x 需要满足 op(x, e) == x 且 op(e, x) == x。
  比如 加法0、乘法1、max=-float('inf')、min=float('inf')、^=0, gcd=0, &=-1
- v: 初始数组
- f: 比较函数。需要满足 f(e) == True
- max_right: 从L开始向右搜索，返回第一个不满足的坐标R。即返回满足区间 [L, R)
- min_left:  从R开始向左搜索，返回最后一个满足的坐标L。即返回满足区间 [L, R)

forked: https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
"""


def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class SegTree:
    def __init__(self, op, e, v):
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p, x):
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left, right):
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

    def max_right(self, left, f):
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right, f):
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


if __name__ == "__main__":
    # RMQ
    data = [1, 3, 2, 7, 9, 11]
    # 定义操作和单位元
    op = min
    e = float("inf")
    st = SegTree(op, e, data)
    # 查询区间 [1, 4) 的最小值 -> min(3, 2, 7) = 2
    print("min [1, 4)", st.prod(1, 4))
    # 将索引 2 的值改为 10 (原先是 2)
    st.set(2, 10)
    # 再次查询区间 [1, 4) -> min(3, 10, 7) = 3
    print("min [1, 4)", st.prod(1, 4))

    # 区间和
    nums = [1, 3, 5, 7, 9, 11]
    st = SegTree(lambda x, y: x + y, 0, nums)
    print(f"区间 [1, 3] 的和: {st.prod(1, 4)}")  # 输出: 3+5+7 = 15
    print(f"总和: {st.all_prod()}")
    st.set(2, 10)  # 将 index 2 的值由 5 改为 10
    print(f"索引2 = {st.get(2)}")
    print(f"更新后区间 [1, 3] 的和: {st.prod(1, 4)}")  # 输出: 3+10+7 = 20
    print(f"总和: {st.all_prod()}")

    # 树上二分
    # 比直接搜快 O(logn)
    data = [2, 3, 1, 5, 8, 2]
    st = SegTree(max, -float("inf"), data)

    r = st.max_right(0, lambda x: x < 7)
    print(f"满足 >= 8 的最小坐标: {r}")  # 输出 4
    r = st.max_right(0, lambda x: x < 100)
    print(f"满足 >= 100 的最小坐标: {r}")  # 输出 6

    r = st.min_left(len(data), lambda x: x < 3)
    print(f"满足 >= 3 的最大坐标: {r - 1}")  # 输出 5
    r = st.min_left(len(data), lambda x: x < 100)
    print(f"满足 >= 100 的最大坐标: {r - 1}")  # 输出 -1
