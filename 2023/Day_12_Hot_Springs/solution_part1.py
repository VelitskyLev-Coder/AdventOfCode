import itertools
from typing import NamedTuple, Optional


class SpringInfo(NamedTuple):
    condition_record: list[str]
    protect_list: list[int]


def get_input() -> list[SpringInfo]:
    result = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            if not line.strip():
                continue
            condition_record_str, protected_list_str = line.split()
            result.append(SpringInfo(list(condition_record_str), list(map(int, protected_list_str.split(',')))))
    return result


def generate_sums(target_sum: int, max_length: int, current_sum: Optional[list[int]] = None):
    if not current_sum:
        current_sum = list()

    if len(current_sum) == max_length:
        if sum(current_sum) == target_sum:
            yield current_sum
        return

    if len(current_sum) == 0 or len(current_sum) == max_length - 1:
        range_start = 0
    else:
        range_start = 1

    rang_end = target_sum - sum(current_sum) + 1

    for i in range(range_start, rang_end + 1):
        yield from generate_sums(target_sum, max_length, current_sum + [i])


def generate_arrangements(total_length: int, protect_list: list[int]):
    for gap_length_list in generate_sums(total_length - sum(protect_list), len(protect_list) + 1):
        cur_list = list()
        for protected_num, gap in zip(itertools.chain([0], protect_list), gap_length_list):
            cur_list.extend('#' * protected_num)
            cur_list.extend('.' * gap)
        yield cur_list


def is_good_arrangement(arrangement: list[str], condition_record: list[str]) -> bool:
    for new, record in zip(arrangement, condition_record):
        if record != '?' and new != record:
            return False
    return True


def get_count_of_arrangements(spring_info: SpringInfo):
    result_count = 0
    for arrangement in generate_arrangements(len(spring_info.condition_record), spring_info.protect_list):
        if is_good_arrangement(arrangement, spring_info.condition_record):
            result_count += 1
    return result_count


def main():
    spring_infos = get_input()
    valid_arrangements_sum = 0
    for spring_info in spring_infos:
        valid_arrangements_sum += get_count_of_arrangements(spring_info)

    print(valid_arrangements_sum)


if __name__ == '__main__':
    main()
