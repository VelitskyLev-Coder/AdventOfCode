import itertools


def walk(grid: list[list[str]]) -> None:
    rows = len(grid)
    cols = len(grid[0])

    guard_direction_ch_list = ['^', '>', '<', 'v']
    direction_ch = None
    for i, row_list in enumerate(grid):
        for j, ch in enumerate(row_list):
            if ch in guard_direction_ch_list:
                direction_ch = ch
                row = i
                col = j
                break
        else:
            continue
        break

    if not direction_ch:
        raise ValueError('No guard found!')


    cur_direction = {
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }.get(direction_ch)

    next_dir_map = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0)
    }

    while True:
        # noinspection PyUnboundLocalVariable
        grid[row][col] = 'X'
        d_row, d_col = cur_direction
        next_row, next_col = row+d_row, col+d_col
        if next_row < 0 or next_col < 0 or next_col >= cols or next_row >= rows:
            break
        if grid[next_row][next_col] == '#':
            cur_direction = next_dir_map[cur_direction]
            continue

        row, col = next_row, next_col



def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(list(line.strip()))

    print('\n'.join([' '.join(row) for row in grid]))
    walk(grid)
    print('_'*100)
    print('\n'.join([' '.join(row) for row in grid]))

    print(list(itertools.chain(*grid)).count('X'))

if __name__ == '__main__':
    main()