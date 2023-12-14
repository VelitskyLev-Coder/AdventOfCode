import itertools

from lava_map_src import DishMap
from solution_part1 import get_input

"""Runtime ~1 min"""


def main():
    dish_map = DishMap(get_input())
    target = 10 ** 9
    history_dict = dict()
    history_dict[dish_map.get_as_long_string()] = 0
    for i in itertools.count(1):
        dish_map.perform_cycle()
        dish_as_string = dish_map.get_as_long_string()
        if dish_as_string in history_dict:
            break
        else:
            history_dict[dish_as_string] = i

    # noinspection PyUnboundLocalVariable
    offset = (target - history_dict[dish_as_string]) % (i - history_dict[dish_as_string])
    real_target = history_dict[dish_as_string] + offset

    dish_map = DishMap(get_input())
    for i in range(real_target):
        dish_map.perform_cycle()
    print(dish_map.calculate_cost())


if __name__ == '__main__':
    main()
