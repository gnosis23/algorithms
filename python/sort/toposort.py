"""
拓扑排序
"""

from collections import deque, defaultdict


def topo_sort(n: int, edges: list[list[int]]) -> list[int]:
    """
    n 个节点的图，给定依赖关系（a->b）列表，输出拓扑排序
    同一个节点可以依赖多个节点
    """
    in_counts = [0] * n
    parents = defaultdict(list)

    for e in edges:
        in_counts[e[1]] += 1
        parents[e[0]].append(e[1])

    queue = deque()
    result = []

    for i in range(n):
        if not in_counts[i]:
            queue.append(i)

    while queue:
        head = queue.popleft()
        result.append(head)

        if head in parents:
            parent_list = parents[head]
            for parent in parent_list:
                in_count = in_counts[parent] - 1
                in_counts[parent] = in_count

                if not in_count:
                    queue.append(parent)

    return result


def main():
    # 0 -> 1 -> 2 -> 4 -> 8
    edges = [[0, 1], [1, 2], [2, 4], [4, 8]]
    results = topo_sort(10, edges)

    print(results)  # [0, 3, 5, 6, 7, 9, 1, 2, 4, 8]


main()
