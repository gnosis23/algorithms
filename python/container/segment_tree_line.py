"""
线段树-扫描线
"""


class TreeNode:
    __slots__ = "l", "r", "min_cover_len", "min_cover", "todo"

    def __init__(self):
        self.l = 0
        self.r = 0
        self.min_cover_len = 0  # 区间内被矩形覆盖次数最少的底边长之和
        self.min_cover = 0  # 区间内被矩形覆盖的最小次数
        self.todo = 0  # 懒标记


class SegmentTree:
    def __init__(self, xs):
        n = len(xs) - 1  # xs.size() 个横坐标有 xs.size()-1 个差值
        self.seg = [TreeNode() for _ in range(2 << (n - 1).bit_length())]
        self.build(xs, 1, 0, n - 1)

    def get_uncovered_length(self):
        return 0 if self.seg[1].min_cover else self.seg[1].min_cover_len

    def maintain(self, no):
        ll = self.seg[no * 2]
        rr = self.seg[no * 2 + 1]
        min_val = min(ll.min_cover, rr.min_cover)
        self.seg[no].min_cover = min_val
        # 只统计等于 min_cover 的底边长之和
        self.seg[no].min_cover_len = 0
        if ll.min_cover == min_val:
            self.seg[no].min_cover_len += ll.min_cover_len
        if rr.min_cover == min_val:
            self.seg[no].min_cover_len += rr.min_cover_len

    # 仅更新节点信息，不下传懒标记 todo
    def do(self, no, v) -> None:
        self.seg[no].min_cover += v
        self.seg[no].todo += v

    def pushDown(self, no) -> None:
        v = self.seg[no].todo
        if v:
            self.do(no * 2, v)
            self.do(no * 2 + 1, v)
            self.seg[no].todo = 0

    def build(self, xs, no, L, R):
        self.seg[no].l = L
        self.seg[no].r = R
        if L == R:
            self.seg[no].min_cover_len = xs[L + 1] - xs[L]
            return
        m = (L + R) // 2
        self.build(xs, no * 2, L, m)
        self.build(xs, no * 2 + 1, m + 1, R)
        self.maintain(no)

    def update(self, no, L, R, v) -> None:
        if L <= self.seg[no].l and self.seg[no].r <= R:
            self.do(no, v)
            return
        self.pushDown(no)
        mid = (self.seg[no].l + self.seg[no].r) // 2
        if L <= mid:
            self.update(no * 2, L, R, v)
        if mid < R:
            self.update(no * 2 + 1, L, R, v)
        self.maintain(no)
