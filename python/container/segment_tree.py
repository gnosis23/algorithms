class SegmentTree:
    def __init__(self, n):
        # 容量为2的整数幂
        self.n = 1
        while self.n < n:
            self.n *= 2
        # 初始化
        self.tree = [0] * (2 * self.n - 1)

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

        # 更新
        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query(self, L, R):
        """
        查询区间 [L, R] 的和
        位置从0开始索引
        """
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if L <= start and end <= R:
            return self.tree[node]

        if end < L or start > R:
            return 0

        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, L, R)
        right_sum = self._query(2 * node + 2, mid + 1, end, L, R)

        return left_sum + right_sum


if __name__ == "__main__":
    # 使用示例
    nums = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(len(nums))
    for idx, num in enumerate(nums):
        st.update(idx, num)

    print(f"区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+5+7 = 15
    st.update(2, 10)  # 将 index 2 的值由 5 改为 10
    print(f"更新后区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+10+7 = 20
