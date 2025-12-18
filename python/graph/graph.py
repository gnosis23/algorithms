from collections import defaultdict
import typing


class SimpleGraph:
    """
    有向带权图，不支持重复边
    """

    def __init__(self):
        self.graph: typing.DefaultDict[int, dict[int, int]] = defaultdict(dict)

    def add_edge(self, u: int, v: int, w: int = 0):
        self.graph[u][v] = w

    def __iter__(self):
        return iter(self.graph)


def main():
    g = SimpleGraph()

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in g.graph[v]:
            print(f"{v} -> {w} = {g.graph[v][w]}")


main()
