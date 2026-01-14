"""
线段树
节点从 1 开始，左节点 no * 2, 右节点 no * 2 + 1
查询索引从 0 开始
"""


class SegmentTree:
    def __init__(self, arr, default=0):
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        self.n = n
        self.w = [0] * (2 << (n - 1).bit_length())
        self.build(arr, 1, 0, n - 1)

    def merge_val(self, a, b):
        """更新: 加法, min/max..."""
        return a + b

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


if __name__ == "__main__":
    # 使用示例
    nums = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(len(nums))
    for idx, num in enumerate(nums):
        st.update(idx, num)

    print(f"区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+5+7 = 15
    st.update(2, 10)  # 将 index 2 的值由 5 改为 10
    print(f"更新后区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+10+7 = 20

    st = SegmentTree(nums)

    print(f"区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+5+7 = 15
    st.update(2, 10)  # 将 index 2 的值由 5 改为 10
    print(f"更新后区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+10+7 = 20
