from typing import Optional


def count_word_here(grid: list[str], row: int, col: int, word: str, direction: Optional[tuple[int, int]] = None) -> int:
    if not word:
        return 1

    rows = len(grid)
    cols = len(grid[0])

    if row<0 or col<0 or col>=cols or row>=rows:
        return 0

    if word[0] != grid[row][col]:
        return 0

    if direction:
        directions = [direction]
    else:
        directions = (
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
        )

    result = 0
    for d_row, d_col in directions:
        if count_word_here(grid, row + d_row, col + d_col, word[1:], direction=(d_row, d_col)):
            result += 1
    return result


def main():
    grid = []
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                grid.append(line.strip())

    rows = len(grid)
    cols = len(grid[0])

    word = 'XMAS'
    result = 0
    for i in range(rows):
        for j in range(cols):
            result += count_word_here(grid, i, j, word)
    print(result)

if __name__ == '__main__':
    main()