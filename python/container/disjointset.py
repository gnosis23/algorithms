"""
并查集
- 带高度和路径压缩
- n 从 0 开始
"""


class DisjointSet:
    def __init__(self, n: int):
        self.p = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.p[i] = i

    def in_same(self, u: int, v: int) -> bool:
        return self.find_set(u) == self.find_set(v)

    def join(self, u: int, v: int) -> None:
        if self.find_set(u) != self.find_set(v):
            self._link(self.find_set(u), self.find_set(v))

    def find_set(self, u: int) -> int:
        if u != self.p[u]:
            self.p[u] = self.find_set(self.p[u])
        return self.p[u]

    def _link(self, u: int, v: int) -> None:
        if self.rank[u] > self.rank[v]:
            self.p[v] = u
        else:
            self.p[u] = v
            if self.rank[u] == self.rank[v]:
                self.rank[u] = self.rank[v] + 1
