import heapq
from enum import Enum, auto
from typing import NamedTuple, Iterator


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

    def __lt__(self, other):
        return self.name < other.name


dir_to_dr = {
    Direction.LEFT: 0,
    Direction.RIGHT: 0,
    Direction.UP: -1,
    Direction.DOWN: 1,
}
dir_to_dc = {
    Direction.LEFT: -1,
    Direction.RIGHT: 1,
    Direction.UP: 0,
    Direction.DOWN: 0,
}


class Vertex(NamedTuple):
    row: int
    column: int
    direction: Direction
    consecutive_blocks: int


class SpecialVertex(Enum):
    START = auto()
    END = auto()


class Edge(NamedTuple):
    source: Vertex | SpecialVertex
    destination: Vertex | SpecialVertex
    weight: int


class Graph:
    def __init__(self):
        self._vertices = set()
        self._edges: dict[Vertex, set[Edge]] = dict()

    def add_vertex(self, vertex: Vertex | SpecialVertex):
        self._vertices.add(vertex)

    def add_edge(self, edge: Edge):
        if edge.source not in self._vertices:
            raise ValueError(f'{edge.source} vertex in not belong to graph, can not add edge {edge}')
        if edge.destination not in self._vertices:
            raise ValueError(f'{edge.destination} vertex in not belong to graph, can not add edge {edge}')
        self._vertices.add(edge.source)
        self._vertices.add(edge.destination)
        self._edges.setdefault(edge.source, set()).add(edge)

    def get_vertices(self) -> Iterator[Vertex]:
        return iter(self._vertices)

    def get_edge(self, source, destination) -> Edge:
        for v in self._edges[source]:
            if v.destination == destination:
                return v

    def get_neighbors_by_vertex(self, vertex: Vertex) -> set[Vertex]:
        return {edge.destination for edge in self._edges.get(vertex, set())}

    def dijkstra(self, source: Vertex | SpecialVertex) \
            -> tuple[dict[Vertex | SpecialVertex, int], dict[Vertex | SpecialVertex, Vertex]]:
        distance = {vertex: float('inf') for vertex in self._vertices}
        previous = {vertex: None for vertex in self._vertices}
        distance[source] = 0
        queue = [(0, source)]

        while queue:
            dist_u, u = heapq.heappop(queue)

            # Skip processing if the distance is outdated
            if dist_u > distance[u]:
                continue

            for v in self.get_neighbors_by_vertex(u):
                alt_distance = distance[u] + self.get_edge(u, v).weight
                if alt_distance < distance[v]:
                    distance[v] = alt_distance
                    previous[v] = u
                    heapq.heappush(queue, (alt_distance, v))

        return distance, previous
