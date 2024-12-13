import copy
import itertools


def dfs(edges_map: dict[tuple, set[tuple]], start: tuple) -> set[tuple]:
    visited: set[tuple] = set()
    stack: list[tuple] = [start]

    while stack:
        top = stack.pop()
        if top in visited:
            continue
        visited.add(top)
        for neighbour in edges_map.get(top, set()):
            if neighbour not in visited:
                stack.append(neighbour)

    return visited


def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(list(line.strip()))

    rows = len(grid)
    cols = len(grid[0])

    edges_map: dict[tuple[int, int], set[tuple[int, int]]] = dict()
    fence_edges_map: dict[tuple[int, int, int, int], set[tuple[int, int, int, int]]] = dict()
    fence_perimeter_bulks: list[list[set[tuple[int, int, int, int]]]] = [[set() for _ in row] for row in grid]
    for i in range(rows):
        for j in range(cols):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbour_i = i+di
                neighbour_j = j+dj
                if di == 0:
                    di_dj_fence = [(1, 0), (-1, 0)]
                else:
                    di_dj_fence = [(0, 1), (0, -1)]
                for di_fence, dj_fence in di_dj_fence:
                    (fence_edges_map.setdefault((i, j, di_fence, dj_fence), set())
                     .add((neighbour_i, neighbour_j, di_fence, dj_fence)))
                if neighbour_i<0 or neighbour_i>=rows or neighbour_j<0 or neighbour_j>=cols:
                    fence_perimeter_bulks[i][j].add((i, j, di, dj))
                    continue
                if grid[neighbour_i][neighbour_j] == grid[i][j]:
                    edges_map.setdefault((i, j), set()).add((neighbour_i, neighbour_j))
                else:
                    fence_perimeter_bulks[i][j].add((i, j, di, dj))


    result = 0
    remaining_cells = set(itertools.product(range(rows), range(cols)))
    while remaining_cells:
        print(len(remaining_cells))
        cur_cell = next(iter(remaining_cells))
        region_set = dfs(edges_map, cur_cell)
        cur_fence_set: set[tuple[int, int, int, int]] = set()
        for i, j in region_set:
            cur_fence_set.update(fence_perimeter_bulks[i][j])

        cur_fence_edges_map = copy.deepcopy(fence_edges_map)
        for (fi, fj, fdi, fdj), n_set in cur_fence_edges_map.items():
            if (fi, fj, fdi, fdj) not in cur_fence_set:
                # n_set.clear()
                pass
            n_set.difference_update(set([(a, b, c, d) for a, b, c, d in n_set if (a, b, c, d) not in cur_fence_set]))

        cur_blocks_num = 0
        while cur_fence_set:
            cur_fence_item = next(iter(cur_fence_set))
            cur_fence_line = dfs(cur_fence_edges_map, cur_fence_item)
            cur_blocks_num += 1
            cur_fence_set.difference_update(cur_fence_line)

        cur_region_area = len(region_set)
        result += cur_blocks_num*cur_region_area
        remaining_cells.difference_update(region_set)

    print(result)



if __name__ == '__main__':
    main()