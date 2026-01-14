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
        self.n = n
        self.w = [0] * (2 << (n - 1).bit_length())
        self.build(arr, 1, 0, n - 1)

    def merge_val(self, a, b):
        """更新: 加法, min/max..."""
        return max(a, b)

    def maintain(self, no):
        """合并左右儿子"""
        self.w[no] = self.merge_val(self.w[no * 2], self.w[no * 2 + 1])

    def build(self, arr, no, L, R):
        if L == R:
            self.w[no] = arr[L]
            return
        mid = (L + R) // 2
        self.build(arr, no * 2, L, mid)
        self.build(arr, no * 2 + 1, mid + 1, R)
        self.maintain(no)

    def _update(self, no, L, R, index, val):
        if L == R:
            self.w[no] = val
            return
        mid = (L + R) // 2
        if index <= mid:  # 在左边
            self._update(no * 2, L, mid, index, val)
        else:
            self._update(no * 2 + 1, mid + 1, R, index, val)
        self.maintain(no)

    def update(self, index, val):
        """将索引 idx 的值更新为 val"""
        self._update(1, 0, self.n - 1, index, val)

    def _query(self, no, L, R, ql, qr):
        if ql <= L and R <= qr:
            return self.w[no]
        mid = (L + R) // 2
        # 剪枝优化：保证进入的递归区间必然相交
        if qr <= mid:
            return self._query(no * 2, L, mid, ql, qr)
        if ql > mid:
            return self._query(no * 2 + 1, mid + 1, R, ql, qr)
        left_val = self._query(no * 2, L, mid, ql, qr)
        right_val = self._query(no * 2 + 1, mid + 1, R, ql, qr)
        return self.merge_val(left_val, right_val)

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)

    def query_pos(self, no, L, R, ql, qr, k):
        """查找范围内>=k的第一个位置"""
        if self.w[no] < k:
            return -1
        # 到达叶子结点，必然 >= k
        if L == R:
            return L
        mid = (L + R) // 2
        if qr <= mid:
            return self.query_pos(no * 2, L, mid, ql, qr, k)
        if ql > mid:
            return self.query_pos(no * 2 + 1, mid + 1, R, ql, qr, k)
        left_val = self.query_pos(no * 2, L, mid, ql, qr, k)
        if left_val != -1:
            return left_val
        return self.query_pos(no * 2 + 1, mid + 1, R, ql, qr, k)


if __name__ == "__main__":
    # 使用示例
    nums = [4, 1, 2, 3, 5]
    st = SegmentTree(nums)

    print("首个满足>=2的位置", st.query_pos(1, 0, st.n - 1, 0, st.n - 1, 2))  # 0
    print("首个满足>=5的位置", st.query_pos(1, 0, st.n - 1, 0, st.n - 1, 5))  # 4
    print("首个满足>=8的位置", st.query_pos(1, 0, st.n - 1, 0, st.n - 1, 8))  # -1

    st.update(2, 10)  # 将 index 2 的值由 5 改为 10
    print("首个满足>=8的位置", st.query_pos(1, 0, st.n - 1, 0, st.n - 1, 8))  # 2
