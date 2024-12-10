
def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(list(map(int, line.strip())))

    rows = len(grid)
    cols = len(grid[0])

    grid_dt = [[0 for _ in row] for row in grid]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                grid_dt[i][j] = 1

    for cur_level in range(0, 8+1):
        for i in range(rows):
            for j in range(cols):
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    neighbour_i = i+di
                    neighbour_j = j+dj
                    if neighbour_i<0 or neighbour_i>=rows or neighbour_j<0 or neighbour_j>=cols:
                        continue
                    if grid[i][j] != cur_level:
                        continue
                    if grid[neighbour_i][neighbour_j] == cur_level + 1:
                        grid_dt[neighbour_i][neighbour_j] += grid_dt[i][j]

    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==9:
                result += grid_dt[i][j]

    print(result)


if __name__ == '__main__':
    main()