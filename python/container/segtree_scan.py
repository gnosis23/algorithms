"""
线段树-扫描线
"""


class ScanLineSegTree:
    def __init__(self, y_coords):
        self.y = y_coords  # 离散化后的 Y 坐标点
        self.n = len(y_coords) - 1
        self.cnt = [0] * (4 * self.n)  # 覆盖次数
        self.length = [0] * (4 * self.n)  # 被覆盖的实际长度

    def _push_up(self, node, L, R):
        if self.cnt[node] > 0:
            # 如果该区间覆盖次数 > 0，则长度为该区间的物理全长
            self.length[node] = self.y[R + 1] - self.y[L]
        elif L == R:
            # 如果是叶子节点且没被覆盖，长度为 0
            self.length[node] = 0
        else:
            # 否则，长度由左右子节点之和决定
            self.length[node] = self.length[2 * node] + self.length[2 * node + 1]

    def update(self, node, L, R, qL, qR, val):
        if qL <= L and R <= qR:
            self.cnt[node] += val
            self._push_up(node, L, R)
            return

        mid = (L + R) // 2
        if qL <= mid:
            self.update(2 * node, L, mid, qL, qR, val)
        if qR > mid:
            self.update(2 * node + 1, mid + 1, R, qL, qR, val)
        self._push_up(node, L, R)


def solve_rect_area(rects):
    if not rects:
        return 0

    events = []
    y_set = set()
    for x1, y1, x2, y2 in rects:
        # 保证 y1 < y2, x1 < x2
        y1, y2 = min(y1, y2), max(y1, y2)
        x1, x2 = min(x1, x2), max(x1, x2)
        # 记录事件：(x坐标, 入/出标记, y1, y2)
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
        y_set.add(y1)
        y_set.add(y2)

    # 1. 坐标离散化
    sorted_y = sorted(list(y_set))
    y_map = {val: i for i, val in enumerate(sorted_y)}

    # 2. 按照 X 轴排序扫描线
    events.sort()

    st = ScanLineSegTree(sorted_y)
    total_area = 0

    # 3. 开始扫描
    for i in range(len(events) - 1):
        x, type, y1, y2 = events[i]
        # 更新线段树：在 Y 轴区间 [y1, y2) 增加覆盖次数
        # 注意：线段树节点 i 代表区间 [sorted_y[i], sorted_y[i+1]]
        st.update(1, 0, st.n - 1, y_map[y1], y_map[y2] - 1, type)

        # 计算当前步长的面积：当前激活长度 * 到下一个事件点的距离
        width = events[i + 1][0] - x
        total_area += st.length[1] * width

    return total_area


# 使用例子
# 两个矩形：(0,0)到(2,2) 和 (1,1)到(3,3)
rects = [(0, 0, 2, 2), (1, 1, 3, 3)]
print(f"矩形面积并: {solve_rect_area(rects)}")  # 输出 7 (4 + 4 - 1重叠)
