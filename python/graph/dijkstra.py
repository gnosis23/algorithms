from collections import namedtuple
from heapq import heappush, heappop

INF = 10**18
Edge = namedtuple("Edge", ["to", "weight"])


def dijkstra(graph: list[list[Edge]], source: int) -> list[int]:
    """
    单源最短路 O(ElogV)
    node_count 默认为 graph 长度
    注意初始化 graph: graph = [[] for _ in range(node_count)]
    """
    node_count = len(graph)
    dist = [INF] * node_count
    dist[source] = 0
    queue: list[tuple[int, int]] = []
    heappush(queue, (0, source))

    while queue:
        cost, v = heappop(queue)
        if dist[v] < cost:
            continue
        for edge in graph[v]:
            if dist[edge.to] > (dist[v] + edge.weight):
                dist[edge.to] = dist[v] + edge.weight
                heappush(queue, (dist[edge.to], edge.to))

    return dist


def main():
    graph = [
        [Edge(1, 10), Edge(4, 15)],
        [Edge(2, 15), Edge(3, 2)],
        [Edge(5, 5)],
        [Edge(2, 1), Edge(5, 12)],
        [Edge(5, 10)],
        [],
    ]
    print(dijkstra(graph, 0))

    graph = [[], [Edge(0, 1), Edge(2, 1)], [Edge(3, 1)], []]
    print(dijkstra(graph, 1))


main()
