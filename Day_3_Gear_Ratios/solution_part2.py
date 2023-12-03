import functools
import operator
from collections import defaultdict
from solution_part1 import get_input, Board


def main():
    board = Board(get_input())
    all_numbers_on_board = board.get_all_numbers()
    gear_dict = defaultdict(list)
    for number in all_numbers_on_board:
        for point in number.get_all_neighbours():
            if board.get_ch_by_point(point) == '*':
                gear_dict[point].append(number.number)

    real_gear_dict = {point: number_list for point, number_list in gear_dict.items() if len(number_list) > 1}

    print(sum(functools.reduce(operator.mul, n_list) for n_list in real_gear_dict.values()))


if __name__ == '__main__':
    main()
