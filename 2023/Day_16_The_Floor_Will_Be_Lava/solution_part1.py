import functools
import itertools
import operator
from enum import Enum, auto
import sys


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


def get_input() -> list[list[str]]:
    with open('input_1.txt') as input_stram:
        return [list(row) for row in input_stram.read().split()]


def propagate_lite(cur_direction: Direction, row: int, column: int, layout: list[list[str]],
                   heat_map_per_direction: dict[Direction, list[list[bool]]]):
    if not (0 <= row < len(layout) and 0 <= column < len(layout[0])):
        return
    if heat_map_per_direction[cur_direction][row][column]:
        return
    heat_map_per_direction[cur_direction][row][column] = True
    ch = layout[row][column]
    new_directions = []
    match (ch, cur_direction):
        case ('.', _) | ('|', Direction.UP) | ('|', Direction.DOWN) | ('-', Direction.RIGHT) | ('-', Direction.LEFT):
            new_directions = [cur_direction]
        case ('|', Direction.RIGHT) | ('|', Direction.LEFT):
            new_directions = [Direction.UP, Direction.DOWN]
        case ('-', Direction.UP) | ('-', Direction.DOWN):
            new_directions = [Direction.RIGHT, Direction.LEFT]
        case ('/', Direction.RIGHT) | ('\\', Direction.LEFT):
            new_directions = [Direction.UP]
        case ('/', Direction.LEFT) | ('\\', Direction.RIGHT):
            new_directions = [Direction.DOWN]
        case ('/', Direction.UP) | ('\\', Direction.DOWN):
            new_directions = [Direction.RIGHT]
        case ('/', Direction.DOWN) | ('\\', Direction.UP):
            new_directions = [Direction.LEFT]

    next_row_and_col_by_direction = {
        Direction.LEFT: (row, column - 1),
        Direction.RIGHT: (row, column + 1),
        Direction.UP: (row - 1, column),
        Direction.DOWN: (row + 1, column),
    }

    for new_direction in new_directions:
        new_row, new_column = next_row_and_col_by_direction[new_direction]
        propagate_lite(new_direction, new_row, new_column, layout, heat_map_per_direction)


def calculate_energized_tiles_number(layout, row, column, direction):
    heat_map_per_direction = {direction: [[False for _ in row] for row in layout] for direction in Direction}
    sys.setrecursionlimit(len(layout) * len(layout[0])*2)
    propagate_lite(direction, row, column, layout, heat_map_per_direction)
    result_heat_map: list[list[str]] = [['.' for _ in row] for row in layout]
    for i, row in enumerate(layout):
        for j, _ in enumerate(row):
            val = functools.reduce(operator.or_, [heat_map_per_direction[direction][i][j] for direction in Direction])
            if val:
                result_heat_map[i][j] = '#'
    # for row in result_heat_map:
    #     print(''.join(row))
    # print()
    result = list(itertools.chain(*result_heat_map)).count('#')
    return result


def main():
    layout = get_input()
    result = calculate_energized_tiles_number(layout, 0, 0, Direction.RIGHT)
    print(result)


if __name__ == '__main__':
    main()
