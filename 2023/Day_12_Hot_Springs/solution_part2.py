from typing import Optional

from solution_part1 import SpringInfo, is_good_arrangement
import functools


def get_input() -> list[SpringInfo]:
    result = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            if not line.strip():
                continue
            condition_record_str, protected_list_str = line.split()
            condition_record_str = '?'.join([condition_record_str for _ in range(5)])
            result.append(SpringInfo(list(condition_record_str), list(map(int, protected_list_str.split(','))) * 5))
    return result


@functools.lru_cache(maxsize=2 ** 20)
def get_count_of_arrangements_rec(condition_record: str, protected_tuple: Optional[tuple[int]],
                                  must_be_gap: bool = False):
    if not condition_record:
        if protected_tuple:
            return 0
        else:
            return 1

    result = 0

    can_fit_gap = condition_record[0] in ('.', '?')
    if can_fit_gap:
        result += get_count_of_arrangements_rec(condition_record[1:], protected_tuple)

    if protected_tuple and len(condition_record) >= protected_tuple[0]:
        can_fit_protected = is_good_arrangement(list('#' * protected_tuple[0]),
                                                list(condition_record[:protected_tuple[0]]))
    else:
        can_fit_protected = False

    if can_fit_protected and not must_be_gap:
        result += get_count_of_arrangements_rec(condition_record[protected_tuple[0]:], tuple(protected_tuple[1:]), True)

    return result


def main():
    spring_infos = get_input()
    valid_arrangements_sum = 0
    for spring_info in spring_infos:
        count = get_count_of_arrangements_rec(''.join(spring_info.condition_record), tuple(spring_info.protect_list))
        valid_arrangements_sum += count

    print(valid_arrangements_sum)


if __name__ == '__main__':
    main()
