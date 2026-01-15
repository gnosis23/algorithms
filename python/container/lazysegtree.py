"""
线段树-支持区间更新
区间为[0, n)，左闭右开

参数解释：
- op: 二元运算符，必须满足结合律。如加法、乘法、最大值、最小值、位运算等等
- e: 单位元。对于 x 需要满足 op(x, e) == x 且 op(e, x) == x。
  比如 加法0、乘法1、max=-float('inf')、min=float('inf')、^=0, gcd=0, &=-1
- v: 初始数组
- f: 比较函数。需要满足 f(e) == True
- max_right: 从L开始向右搜索，返回第一个不满足的坐标R。即返回满足区间 [L, R)
- min_left:  从R开始向左搜索，返回最后一个满足的坐标L。即返回满足区间 [L, R)
- apply(l, r, x): 区间 [l, r) + x
- mapping(f, x): 如何将懒标记 f 应用到节点数据 x 上
- composition(f, g): 如何合并两个懒标记（新标记 f 应用在旧标记 g 上）
- id_: 懒标记的单位元（表示“无操作”）

forked: https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py
"""


def _ceil_pow2(n):
    x = 0
    while (1 << x) < n:
        x += 1

    return x


class LazySegTree:
    def __init__(self, op, e, mapping, composition, id_, v):
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p, x):
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left, right):
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        sml = self._e
        smr = self._e
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

    def apply(self, left, right=None, f=None):
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(self, left, g):
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right, g):
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k, f):
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k):
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


if __name__ == "__main__":
    # 例1: 区间加，区间求和
    # 数据节点：(当前区间的和, 当前区间的长度)
    # op: 合并两个节点
    def op(node1, node2):
        return (node1[0] + node2[0], node1[1] + node2[1])

    e = (0, 0)

    # mapping: f 是要加的值，x 是 (sum, size)
    def mapping(f, x):
        return (x[0] + f * x[1], x[1])

    # composition: 连续两个加法 f 和 g，合并为 f + g
    def composition(f, g):
        return f + g

    id_ = 0

    # 初始化数据
    v = [(val, 1) for val in [1, 2, 3, 4, 5]]
    lst = LazySegTree(op, e, mapping, composition, id_, v)

    # 区间 [0, 3) 加上 10 -> [11, 12, 13, 4, 5]
    lst.apply(0, 3, 10)
    print(lst.prod(0, 5)[0])  # 输出 45

    # 例2: 区间更新，区间最大值
    # op: 求最大值
    def op(x, y):
        return max(x, y)

    e = -float("inf")

    # mapping: 如果标记 f 不是 None，则节点值变为 f
    def mapping(f, x):
        return f if f is not None else x

    # composition: 新标记 f 覆盖旧标记 g
    def composition(f, g):
        return f if f is not None else g

    id_ = None

    v = [1, 5, 2, 4, 3]
    lst = LazySegTree(op, e, mapping, composition, id_, v)

    # 将区间 [1, 4) 全部改为 10 -> [1, 10, 10, 10, 3]
    lst.apply(1, 4, 10)
    print(lst.prod(0, 5))  # 输出 10

    # 例3: 仿射变换
    MOD = 998244353

    def op(node1, node2):
        return ((node1[0] + node2[0]) % MOD, node1[1] + node2[1])

    e = (0, 0)

    # mapping: f=(a, b), x=(sum, size) -> a*sum + b*size
    def mapping(f, x):
        a, b = f
        s, sz = x
        return ((a * s + b * sz) % MOD, sz)

    # composition: 新 f=(a1, b1) 作用于旧 g=(a2, b2)
    # f(g(x)) = a1*(a2*x + b2) + b1 = (a1*a2)*x + (a1*b2 + b1)
    def composition(f, g):
        a1, b1 = f
        a2, b2 = g
        return ((a1 * a2) % MOD, (a1 * b2 + b1) % MOD)

    id_ = (1, 0)  # 1*x + 0 = x

    v = [(x, 1) for x in [1, 2, 3]]
    lst = LazySegTree(op, e, mapping, composition, id_, v)
    # 例子：区间乘以 2 再加 3
    lst.apply(0, 3, (2, 3))
    print(lst.all_prod())
