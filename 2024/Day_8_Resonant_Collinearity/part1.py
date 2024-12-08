import itertools


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
            i_new_1 = i1+(i2-i1)*2
            j_new_1 = j1+(j2-j1)*2
            if 0<=i_new_1<rows and 0<=j_new_1<cols:
                antinode_set.add((i_new_1, j_new_1))

            i_new_2 = i2 + (i1 - i2) * 2
            j_new_2 = j2 + (j1 - j2) * 2
            if 0 <= i_new_2 < rows and 0 <= j_new_2 < cols:
                antinode_set.add((i_new_2, j_new_2))

    print(len(antinode_set))

if __name__ == '__main__':
    main()