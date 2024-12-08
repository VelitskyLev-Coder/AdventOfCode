import itertools
import math


def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(list(line.strip()))

    antennas_map: dict[str, list[tuple[int, int]]] = dict()

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '.':
                antennas_map.setdefault(grid[i][j], list()).append((i, j))

    antinode_set: set[tuple[int, int]]  = set()

    for ch, antennas_coord_list in antennas_map.items():
        for (i1, j1), (i2, j2) in itertools.combinations(antennas_coord_list, 2):
            gcd = math.gcd(abs(i1-i2), abs(j1-j2))
            step_i = (i1-i2)//gcd
            step_j = (j1-j2)//gcd

            max_times = min(rows//step_i, cols//step_j)*2

            step = 1 if max_times>0 else -1
            for i in range(-max_times, max_times+1, step):
                new_i = i1+i*step_i
                new_j = j1+i*step_j
                if 0 <= new_i < rows and 0 <= new_j < cols:
                    antinode_set.add((new_i, new_j))

    for i, j in antinode_set:
        if grid[i][j]=='.':
            grid[i][j] = '#'

    print('\n'.join([''.join(line) for line in grid]))

    print(len(antinode_set))

if __name__ == '__main__':
    main()