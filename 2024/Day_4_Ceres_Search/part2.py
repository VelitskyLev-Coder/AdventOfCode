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
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] != 'A':
                continue
            first_diagonal = (grid[i-1][j-1], grid[i+1][j+1])
            second_diagonal = (grid[i+1][j-1], grid[i-1][j+1])
            if first_diagonal in [('M', 'S'), ('S', 'M')] and second_diagonal in [('M', 'S'), ('S', 'M')]:
                result += 1

    print(result)


if __name__ == '__main__':
    main()