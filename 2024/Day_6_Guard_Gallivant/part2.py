import itertools
from tqdm import tqdm


def walk_with_restore_the_guard(grid: list[list[str]]) -> None:
    # Repeats the wolk from part one. Except it restores the guard
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

    # noinspection PyUnboundLocalVariable
    guard_ch, guard_start_row, guard_start_col = direction_ch, row, col

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
        grid[row][col] = 'X'
        d_row, d_col = cur_direction
        next_row, next_col = row+d_row, col+d_col
        if next_row < 0 or next_col < 0 or next_col >= cols or next_row >= rows:
            break
        if grid[next_row][next_col] == '#':
            cur_direction = next_dir_map[cur_direction]
            continue

        row, col = next_row, next_col

    grid[guard_start_row][guard_start_col] = guard_ch

def has_a_loop(grid: list[list[str]]) -> bool:
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

    history = set()

    while True:
        # noinspection PyUnboundLocalVariable
        if (row, col, cur_direction) in history:
            return True
        history.add((row, col, cur_direction))
        d_row, d_col = cur_direction
        next_row, next_col = row+d_row, col+d_col
        if next_row < 0 or next_col < 0 or next_col >= cols or next_row >= rows:
            break
        if grid[next_row][next_col] == '#':
            cur_direction = next_dir_map[cur_direction]
            continue

        row, col = next_row, next_col

    return False


def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(list(line.strip()))

    rows = len(grid)
    cols = len(grid[0])

    # Optimization. We can try to place an obstacle only where guard will go
    walk_with_restore_the_guard(grid)
    result = 0
    for i, j in tqdm(itertools.product(range(rows), range(cols)), total=rows * cols, desc="Processing"):
        if grid[i][j] == 'X':
            grid[i][j] = '#'
            if has_a_loop(grid):
                result += 1
            grid[i][j] = 'X'

    print(result)

if __name__ == '__main__':
    main()