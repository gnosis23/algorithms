from collections import defaultdict, namedtuple
import typing

LinkedVertex = namedtuple("Vertext", ["node", "weight"])


class LinkedGraph:
    """
    有向带权图，不支持重复边
    """

    def __init__(self):
        self.graph: typing.DefaultDict[int, list[LinkedVertex]] = defaultdict(list)

    def add_edge(self, u: int, v: int, w: int = 0):
        self.graph[u].append(LinkedVertex(v, w))

    def __iter__(self):
        return iter(self.graph)
