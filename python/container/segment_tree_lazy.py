"""
线段树-支持区间更新
节点从 1 开始，左节点 no * 2, 右节点 no * 2 + 1
查询索引从 0 开始
forked: https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
"""


class Node:
    __slots__ = "val", "todo"


class LazySegmentTree:
    # 懒标记初始值
    _TODO_INIT = 0  # 根据题目修改

    def __init__(self, arr, default=0):
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        # 容量为2的整数幂
        self.n = n
        self.tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(arr, 1, 0, n - 1)

    def _merge_val(self, a, b):
        """更新: 根据题目修改"""
        return a + b

    def _merge_todo(self, a, b):
        """更新: 根据题目修改"""
        return a + b

    def _apply(self, node, L, R, todo):
        """将懒标记作用到node"""
        cur = self.tree[node]
        # 根据题目修改, 这里是增量
        cur.val += todo * (R - L + 1)
        cur.todo = self._merge_todo(todo, cur.todo)

    def _spread(self, node, L, R):
        """将当前节点的懒标记下传给儿子"""
        todo = self.tree[node].todo
        if todo == self._TODO_INIT:
            return
        mid = (L + R) // 2
        self._apply(node * 2, L, mid, todo)
        self._apply(node * 2 + 1, mid + 1, R, todo)
        self.tree[node].todo = self._TODO_INIT

    def _maintain(self, node):
        """合并左右儿子"""
        self.tree[node].val = self._merge_val(
            self.tree[node * 2].val, self.tree[node * 2 + 1].val
        )

    def _build(self, arr, node, L, R):
        self.tree[node].todo = self._TODO_INIT
        if L == R:
            self.tree[node].val = arr[L]
            return
        mid = (L + R) // 2
        self._build(arr, node * 2, L, mid)
        self._build(arr, node * 2 + 1, mid + 1, R)
        self._maintain(node)

    def _update(self, node, L, R, ql, qr, val):
        if ql <= L and R <= qr:
            self._apply(node, L, R, val)
            return
        self._spread(node, L, R)
        mid = (L + R) // 2
        # 更新写成这样是为了不错过任何一个受影响的子节点并正确汇总到父节点。
        # 使用的是“双判断”逻辑（如果和左边有交集就去左边，如果和右边有交集就去右边）
        if ql <= mid:
            self._update(node * 2, L, mid, ql, qr, val)
        if qr > mid:
            self._update(node * 2 + 1, mid + 1, R, ql, qr, val)
        self._maintain(node)

    def update(self, ql, qr, val):
        """将索引 [ql, qr] 的值更新为 val"""
        self._update(1, 0, self.n - 1, ql, qr, val)

    def _query(self, node, L, R, ql, qr):
        if ql <= L and R <= qr:
            return self.tree[node].val
        self._spread(node, L, R)
        mid = (L + R) // 2
        # 剪枝优化：保证进入的递归区间必然相交
        # 使用的是“三分支”逻辑（要么只去左，要么只去右，要么左右都去并合并）
        if qr <= mid:
            return self._query(node * 2, L, mid, ql, qr)
        if ql > mid:
            return self._query(node * 2 + 1, mid + 1, R, ql, qr)
        left_val = self._query(node * 2, L, mid, ql, qr)
        right_val = self._query(node * 2 + 1, mid + 1, R, ql, qr)
        return self._merge_val(left_val, right_val)

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)


if __name__ == "__main__":
    # 使用示例
    nums = [1, 3, 5, 7, 9, 11]
    st = LazySegmentTree(nums)

    print(f"区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+5+7 = 15
    st.update(2, 3, 10)  # 将 index 2,3 的值 改为 10
    print(f"更新后区间 [1, 3] 的和: {st.query(1, 3)}")  # 输出: 3+15+17 = 35
