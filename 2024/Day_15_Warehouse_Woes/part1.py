def move(grid: list[list[str]], row: int, col: int, direction: str) -> bool:
    new_row, new_col = get_next_position(row, col, direction)
    if grid[row][col] == '.':
        return True
    if grid[row][col] == '#':
        return False
    can_move = move(grid, new_row, new_col, direction)
    if not can_move:
        return False
    grid[new_row][new_col] = grid[row][col]
    grid[row][col] = '.'
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
                grid.append(list(line.strip()))
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
        if move(grid, cur_row, cur_col, direction):
            cur_row, cur_col = get_next_position(cur_row, cur_col, direction)
        #print(direction)
        #print('\n'.join(''.join(r) for r in grid))
        #print('-'*100)


    result = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                result += 100*i + j

    print(result)

if __name__ == '__main__':
    main()