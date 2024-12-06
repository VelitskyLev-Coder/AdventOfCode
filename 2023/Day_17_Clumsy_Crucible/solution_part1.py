import copy
from typing import Callable

from graph import Direction, dir_to_dr, dir_to_dc, Vertex, Edge, Graph, SpecialVertex


def get_input() -> list[list[int]]:
    with open('input_1.txt') as input_stram:
        return [list(map(int, row)) for row in input_stram.read().split()]


def constrain_part_1(_: Direction, __: Direction, ___, new_consecutive_blocks: int):
    return new_consecutive_blocks <= 3


def init_graph(grid, constrain: Callable[[Direction, Direction, int, int], bool], max_consecutive_blocks: int,
               min_consecutive_blocks_at_the_end=0):
    max_row_index = len(grid) - 1
    max_column_index = len(grid[0]) - 1
    graph = Graph()
    for i, row in enumerate(grid):
        for j, heat_lose in enumerate(row):
            for direction in Direction:
                for consecutive_blocks in range(1, max_consecutive_blocks + 1):
                    graph.add_vertex(Vertex(i, j, direction, consecutive_blocks))
    for vertex in graph.get_vertices():
        for direction in Direction:
            if (dir_to_dr[vertex.direction] + dir_to_dr[direction] == 0 and
                    dir_to_dc[vertex.direction] + dir_to_dc[direction] == 0):
                continue
            row, col = vertex.row + dir_to_dr[direction], vertex.column + dir_to_dc[direction]
            if not (0 <= row <= max_row_index and 0 <= col <= max_column_index):
                continue
            for consecutive_blocks in range(1, max_consecutive_blocks + 1):
                if vertex.direction == direction:
                    dest_consecutive_blocks = vertex.consecutive_blocks + 1
                else:
                    dest_consecutive_blocks = 1
                if not constrain(vertex.direction, direction, vertex.consecutive_blocks, dest_consecutive_blocks):
                    continue
                dest_vertex = Vertex(row, col, direction, dest_consecutive_blocks)
                graph.add_edge(Edge(vertex, dest_vertex, grid[row][col]))
    graph.add_vertex(SpecialVertex.START)
    graph.add_vertex(SpecialVertex.END)
    graph.add_edge(Edge(SpecialVertex.START, Vertex(0, 1, Direction.RIGHT, 1), grid[0][1]))
    graph.add_edge(Edge(SpecialVertex.START, Vertex(1, 0, Direction.DOWN, 1), grid[1][0]))
    for direction in Direction:
        for consecutive_blocks in range(1, max_consecutive_blocks + 1):
            if consecutive_blocks < min_consecutive_blocks_at_the_end:
                continue
            graph.add_edge(
                Edge(Vertex(max_row_index, max_column_index, direction, consecutive_blocks), SpecialVertex.END, 0))
    return graph


def visualize(grid, previous, start_vertex, end_vertex):
    grid_copy = copy.deepcopy(grid)
    path = []
    cur = end_vertex
    while cur != start_vertex:
        path.append(previous[cur])
        cur = previous[cur]
    path = path[:-1]
    for vertex in path:
        grid_copy[vertex.row][vertex.column] = {
            Direction.LEFT: '<',
            Direction.RIGHT: '>',
            Direction.UP: '^',
            Direction.DOWN: 'v',
        }.get(vertex.direction)
    for row in grid_copy:
        print(''.join(map(str, row)))


def main():
    grid = get_input()
    graph = init_graph(grid, constrain_part_1, 3)
    distance, previous = graph.dijkstra(SpecialVertex.START)
    visualize(grid, previous, SpecialVertex.START, SpecialVertex.END)
    print(f'Min heat loss = {distance[SpecialVertex.END]}')


if __name__ == '__main__':
    main()
