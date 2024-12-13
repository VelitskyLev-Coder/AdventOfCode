import itertools


def dfs(edges_map: dict[tuple[int, int], set[tuple[int, int]]], start: tuple[int, int]) -> set[tuple[int, int]]:
    visited: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = [start]

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
    fence_perimeter_grid = [[0 for _ in row] for row in grid]
    for i in range(rows):
        for j in range(cols):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbour_i = i+di
                neighbour_j = j+dj
                if neighbour_i<0 or neighbour_i>=rows or neighbour_j<0 or neighbour_j>=cols:
                    fence_perimeter_grid[i][j] += 1
                    continue
                if grid[neighbour_i][neighbour_j] == grid[i][j]:
                    edges_map.setdefault((i, j), set()).add((neighbour_i, neighbour_j))
                else:
                    fence_perimeter_grid[i][j] += 1

    result = 0
    remaining_cells = set(itertools.product(range(rows), range(cols)))

    while remaining_cells:
        cur_cell = next(iter(remaining_cells))
        region_set = dfs(edges_map, cur_cell)
        cur_region_perimeter = sum(fence_perimeter_grid[i][j] for i,j in region_set)
        cur_region_area = len(region_set)
        result += cur_region_perimeter*cur_region_area
        remaining_cells.difference_update(region_set)

    print(result)



if __name__ == '__main__':
    main()