from solution_part1 import get_input, calculate_energized_tiles_number, Direction


def main():
    layout = get_input()
    row_number = len(layout)
    column_number = len(layout[0])

    configuration_row = []
    configuration_column = []
    configuration_direction = []

    for i in range(column_number):
        configuration_row.append(0)
        configuration_column.append(i)
        configuration_direction.append(Direction.DOWN)
        configuration_row.append(row_number-1)
        configuration_column.append(i)
        configuration_direction.append(Direction.UP)

    for i in range(column_number):
        configuration_row.append(i)
        configuration_column.append(0)
        configuration_direction.append(Direction.RIGHT)
        configuration_row.append(i)
        configuration_column.append(column_number-1)
        configuration_direction.append(Direction.LEFT)

    possible_counts = []
    for row, column, direction in zip(configuration_row, configuration_column, configuration_direction):
        possible_counts.append(calculate_energized_tiles_number(layout, row, column, direction))

    print(max(possible_counts))


if __name__ == '__main__':
    main()
