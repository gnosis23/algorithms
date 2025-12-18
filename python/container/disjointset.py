"""
并查集
- 带高度和路径压缩
- n 从 0 开始
"""


class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def in_same(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)

    def union(self, u: int, v: int) -> bool:
        """
        返回值表示是否发生了合并（原来不在一个集合中）
        """
        if self.find(u) != self.find(v):
            self._merge(self.find(u), self.find(v))
            return True
        return False

    def find(self, u: int) -> int:
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def _merge(self, u: int, v: int) -> None:
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[u] = v
            if self.rank[u] == self.rank[v]:
                self.rank[u] = self.rank[v] + 1
