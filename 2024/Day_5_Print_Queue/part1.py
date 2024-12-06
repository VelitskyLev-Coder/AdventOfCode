
def is_right_order(page_blocker_map: dict[int, set[int]], update: list[int]) -> bool:
    cur_blocked = set()
    for page in update:
        if page in cur_blocked:
            return False
        cur_blocked.add(page)
        cur_blocked.update(page_blocker_map.get(page, set()))

    return True

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

    result = 0
    for update in updates:
        if is_right_order(page_blocker_map, update):
            result += update[len(update)//2]

    print(result)



if __name__ == '__main__':
    main()