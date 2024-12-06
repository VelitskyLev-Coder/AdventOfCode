import functools
import itertools


def is_right_order(page_blocker_map: dict[int, set[int]], update: list[int]) -> bool:
    cur_blocked = set()
    for page in update:
        if page in cur_blocked:
            return False
        cur_blocked.add(page)
        cur_blocked.update(page_blocker_map.get(page, set()))

    return True

def order_right(page_blocker_map: dict[int, set[int]], update: list[int]) -> list[int]:
    left = set(update)
    result = []

    while left:
        next_page = None
        for page in left:
            if not page_blocker_map.get(page, set()).intersection(left):
                next_page = page
                break
        if not next_page:
            raise ValueError(f'Can not find the right order for the {update}')
        left.remove(next_page)
        result.append(next_page)

    return result


def main():
    rules = []
    updates = []
    with open('input.txt') as input_file:
        for line in input_file:
            if not line.strip():
                continue
            if '|' in line:
                rules.append(list(map(int, line.split('|'))))
            else:
                updates.append(list(map(int, line.split(','))))

    page_blocker_map: dict[int, set[int]] = dict()

    for page_before, page_after in rules:
        page_blocker_map.setdefault(page_after, set()).add(page_before)

    incorrect_updates = itertools.filterfalse(functools.partial(is_right_order, page_blocker_map), updates)

    result = 0
    for update in incorrect_updates:
        result += order_right(page_blocker_map, update)[len(update) // 2]

    print(result)


if __name__ == '__main__':
    main()