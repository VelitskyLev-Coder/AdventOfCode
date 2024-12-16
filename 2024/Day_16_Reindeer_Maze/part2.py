from heapq import heappush, heappop
from typing import TypeVar

T = TypeVar('T')
INFINITY = 10**20

def dijkstra(edges_map: dict[T, set[tuple[T, int]]], source: T) -> tuple[dict[T, int], dict[T, set[T]]]:
    dist: dict[T, int] = dict()
    prev: dict[T, set[T]] = dict()
    queue: list[tuple[int, T]] = []

    for vertex in edges_map.keys():
        dist[vertex] = INFINITY
        prev[vertex] = set()

    dist[source] = 0
    heappush(queue, (0, source))

    while queue:
        current_dist, u = heappop(queue)

        if current_dist > dist[u]:
            continue  # Skip outdated entries in the priority queue

        for neighbor, d in edges_map[u]:
            alt = dist[u] + d
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = {u}
                heappush(queue, (alt, neighbor))
            elif alt == dist[neighbor]:
                prev[neighbor].add(u)

    return dist, prev

def find_char_in_grid(grid: list[list[str]], ch: str) -> tuple[int, int]:
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ch:
                return i, j

    raise ValueError(f'Can not find {ch} in a grid')


def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(list(line.strip()))

    rows = len(grid)
    cols = len(grid[0])
    t_position = tuple[int, int]
    t_direction = tuple[int, int]
    t_vertex = tuple[t_position, t_direction]
    edges_map: dict[t_vertex, set[tuple[t_vertex, int]]] = dict()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                continue
            edges_map.setdefault(((i, j), (0, 1)), set()).add((((i, j), (1, 0)), 1000))
            edges_map.setdefault(((i, j), (0, 1)), set()).add((((i, j), (-1, 0)), 1000))
            edges_map.setdefault(((i, j), (0, -1)), set()).add((((i, j), (1, 0)), 1000))
            edges_map.setdefault(((i, j), (0, -1)), set()).add((((i, j), (-1, 0)), 1000))
            edges_map.setdefault(((i, j), (1, 0)), set()).add((((i, j), (0, -1)), 1000))
            edges_map.setdefault(((i, j), (1, 0)), set()).add((((i, j), (0, 1)), 1000))
            edges_map.setdefault(((i, j), (-1, 0)), set()).add((((i, j), (0, -1)), 1000))
            edges_map.setdefault(((i, j), (-1, 0)), set()).add((((i, j), (0, 1)), 1000))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbour_i = i+di
                neighbour_j = j+dj
                if neighbour_i<0 or neighbour_i>=rows or neighbour_j<0 or neighbour_j>=cols:
                    continue
                if grid[neighbour_i][neighbour_j] != '#':
                    edges_map.setdefault(((i, j),(di, dj)), set()).add((((neighbour_i, neighbour_j), (di, dj)),1))


    start_row, start_col = find_char_in_grid(grid, 'S')
    finish_row, finish_col = find_char_in_grid(grid, 'E')

    start_ver = ((start_row, start_col), (0, 1))
    finish_ver_list = [
        ((finish_row, finish_col), (0, 1)),
        ((finish_row, finish_col), (0, -1)),
        ((finish_row, finish_col), (1, 0)),
        ((finish_row, finish_col), (-1, 0)),
    ]

    dist, prev = dijkstra(edges_map, start_ver)

    finish_ver = min(finish_ver_list, key=lambda v: dist[v])

    in_the_best_path = {v for v in finish_ver_list if dist[v]==dist[finish_ver]}
    queue = set(in_the_best_path)
    while queue:
        cur = queue.pop()
        in_the_best_path.add(cur)
        queue.update(prev[cur])

    coord_set = {(i, j) for (i,j) , (_, _) in in_the_best_path}



    for i, j in coord_set:
        grid[i][j] = 'O'

    print('\n'.join(''.join(row) for row in grid))

    print(len(coord_set))

if __name__ == '__main__':
    main()