from lava_map_src import LavaMap


def get_input() -> list[list[str]]:
    result = list()
    with open('input_1.txt') as input_stram:
        cur_list = list()
        for line in input_stram:
            if not line.strip():
                if cur_list:
                    result.append(cur_list)
                    cur_list = list()
                continue
            cur_list.append(line.strip())
        if cur_list:
            result.append(cur_list)

    return result


def main():
    total_sum = 0
    for data in get_input():
        lava_map = LavaMap(data)
        total_sum += sum(lava_map.get_horizontal_reflection_indexes()) * 100
        total_sum += sum(lava_map.get_vertical_reflection_indexes())
    print(total_sum)


if __name__ == '__main__':
    main()
