import copy
from lava_map_src import LavaMap
from solution_part1 import get_input


def main():
    total_sum = 0
    for data in get_input():
        lava_map = LavaMap(data)
        total_sum += sum(lava_map.get_horizontal_reflection_lines_fixed())*100
        total_sum += sum(lava_map.get_vertical_reflection_lines_fixed())
    print(total_sum)

if __name__ == '__main__':
    main()
