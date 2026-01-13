"""
线段树
查询 k 首次出现位置
"""


class SegmentTree:
    def __init__(self, arr, default=0):
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        # 容量为2的整数幂
        self.n = 1
        while self.n < n:
            self.n *= 2
        # 初始化
        self.tree = [0] * (2 * self.n - 1)
        self._build(arr, 0, 0, self.n - 1)

    def _merge(self, a: int, b: int):
        """更新: 加法, min/max..."""
        return max(a, b)

    def _maintain(self, node: int):
        self.tree[node] = self._merge(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def _build(self, arr, node, start, end):
        if start == end:
            if start < len(arr):
                self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self._build(arr, node * 2 + 1, start, mid)
        self._build(arr, node * 2 + 2, mid + 1, end)
        self._maintain(node)

    def update(self, idx, val):
        """将索引 idx 的值更新为 val"""
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        if idx <= mid:
            self._update(left_node, start, mid, idx, val)
        else:
            self._update(right_node, mid + 1, end, idx, val)
        self._maintain(node)

    def query(self, node, start, end, L, R, k):
        """查找范围内>=k的第一个位置"""
        # 不在范围内或者不存在合理的值
        if end < L or start > R or self.tree[node] < k:
            return -1
        # 到达叶子结点，必然 >= k
        if start == end:
            return start
        mid = (start + end) // 2
        res = self.query(node * 2 + 1, start, mid, L, R, k)
        if res == -1:
            return self.query(node * 2 + 2, mid + 1, end, L, R, k)
        return res


if __name__ == "__main__":
    # 使用示例
    nums = [4, 1, 2, 3, 5]
    st = SegmentTree(nums)

    print("首个满足>=2的位置", st.query(0, 0, st.n - 1, 0, st.n - 1, 2))  # 0
    print("首个满足>=5的位置", st.query(0, 0, st.n - 1, 0, st.n - 1, 5))  # 4
    print("首个满足>=8的位置", st.query(0, 0, st.n - 1, 0, st.n - 1, 8))  # -1

    st.update(2, 10)  # 将 index 2 的值由 5 改为 10
    print("首个满足>=8的位置", st.query(0, 0, st.n - 1, 0, st.n - 1, 8))  # 2
