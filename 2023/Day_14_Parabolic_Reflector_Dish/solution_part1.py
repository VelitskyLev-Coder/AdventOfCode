from lava_map_src import DishMap


def get_input() -> list[str]:
    result = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            if not line.strip():
                continue
            result.append(line.strip())
    return result


def main():
    dish_map = DishMap(get_input())
    dish_map.shift_all_top()
    print(dish_map.calculate_cost())


if __name__ == '__main__':
    main()
