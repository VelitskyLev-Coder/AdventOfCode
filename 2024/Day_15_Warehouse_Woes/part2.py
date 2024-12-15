def move(grid: list[list[str]], row: int, col: int, direction: str, allow_move: bool) -> bool:
    if grid[row][col] == '.':
        return True
    if grid[row][col] == '#':
        return False
    if direction in '<>' or grid[row][col] == '@':
        objects = [(row, col)]
    elif grid[row][col] == '[':
        objects = [(row, col), (row, col + 1)]
    else:
        objects = [(row, col), (row, col - 1)]
    for cur_row, cur_col in objects:
        new_row, new_col = get_next_position(cur_row, cur_col, direction)
        if not move(grid, new_row, new_col, direction, allow_move):
            return False
        if allow_move:
            grid[new_row][new_col] = grid[cur_row][cur_col]
            grid[cur_row][cur_col] = '.'

    return True


def get_next_position(row, col, direction):
    d_row, d_col = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }.get(direction)
    new_row = row + d_row
    new_col = col + d_col
    return new_row, new_col


def main():
    grid = []
    movements = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                cur_row_list = []
                for ch in line:
                    if ch == '#':
                        cur_row_list.extend('##')
                    elif ch == 'O':
                        cur_row_list.extend('[]')
                    elif ch == '.':
                        cur_row_list.extend('..')
                    elif ch == '@':
                        cur_row_list.extend('@.')
                grid.append(cur_row_list)
            else:
                break
        while line := input_file.readline().strip():
            movements.extend(line)

    rows = len(grid)
    cols = len(grid[0])

    cur_row = 0
    cur_col = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                cur_row = i
                cur_col = j
                break
        else:
            continue
        break
    #print('\n'.join(''.join(r) for r in grid))
    #print('-' * 100)
    for direction in movements:
        pass
        if move(grid, cur_row, cur_col, direction, allow_move=False):
            move(grid, cur_row, cur_col, direction, allow_move=True)
            cur_row, cur_col = get_next_position(cur_row, cur_col, direction)
        #print(direction)
        #print('\n'.join(''.join(r) for r in grid))
        #print('-'*100)

    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in '[':
                result += 100 * i + j

    print(result)


if __name__ == '__main__':
    main()