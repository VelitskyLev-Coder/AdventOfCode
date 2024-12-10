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
                grid.append(list(map(int, line.strip())))

    rows = len(grid)
    cols = len(grid[0])

    edges_map: dict[tuple[int, int], set[tuple[int, int]]] = dict()

    for i in range(rows):
        for j in range(cols):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbour_i = i+di
                neighbour_j = j+dj
                if neighbour_i<0 or neighbour_i>=rows or neighbour_j<0 or neighbour_j>=cols:
                    continue
                if grid[neighbour_i][neighbour_j] == grid[i][j] + 1:
                    edges_map.setdefault((i, j), set()).add((neighbour_i, neighbour_j))

    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]!=0:
                continue
            reachable = dfs(edges_map, (i, j))
            nines = sum(1 for x, y in reachable if grid[x][y]==9)
            result += nines

    print(result)


if __name__ == '__main__':
    main()