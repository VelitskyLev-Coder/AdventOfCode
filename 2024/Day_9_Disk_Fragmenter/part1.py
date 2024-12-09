import itertools


def main():
    with open('input.txt') as input_file:
        disk_map = input_file.read().strip()

    expanded_list = []

    cur_file_index = 0
    for block_size, is_file in zip(map(int, disk_map), itertools.cycle([True, False])):
        if is_file:
            fill_with = cur_file_index
            cur_file_index += 1
        else:
            fill_with = None
        expanded_list.extend(itertools.repeat(fill_with, block_size))

    defragmented_disk = expanded_list.copy()
    left_idx = 0
    right_idx = len(defragmented_disk) - 1
    while left_idx < right_idx:
        if defragmented_disk[left_idx] is not None:
            left_idx += 1
        elif defragmented_disk[right_idx] is None:
            right_idx -= 1
        else:
            defragmented_disk[left_idx] = defragmented_disk[right_idx]
            defragmented_disk[right_idx] = None

    defragmented_disk = defragmented_disk[:left_idx]

    check_sum = 0
    for position, file_id in enumerate(defragmented_disk):
        check_sum += position*file_id

    print(check_sum)


if __name__ == '__main__':
    main()