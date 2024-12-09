import itertools


def main():
    with open('input.txt') as input_file:
        disk_map = input_file.read().strip()

    expanded_list = []

    pos_to_free_space: dict[int, int] = dict()
    id_to_space: dict[int, int] = dict()
    id_to_start_pos: dict[int, int] = dict()

    cur_file_index = 0
    for block_size, is_file in zip(map(int, disk_map), itertools.cycle([True, False])):
        if is_file:
            fill_with = cur_file_index
            id_to_space[cur_file_index] = block_size
            id_to_start_pos[cur_file_index] = len(expanded_list)
            cur_file_index += 1
        else:
            fill_with = None
            pos_to_free_space[len(expanded_list)] = pos_to_free_space.get(len(expanded_list), 0) + block_size
        expanded_list.extend(itertools.repeat(fill_with, block_size))

    #print(pos_to_free_space)
    #print(id_to_space)
    #print(id_to_start_pos)
    defragmented_disk = expanded_list.copy()

    cur_index = len(expanded_list) - 1

    while cur_index > 0:
        #print(''.join([str(elem) if elem is not None else '.' for elem in defragmented_disk]))
        if defragmented_disk[cur_index] is None:
            cur_index -= 1
        else:
            cur_id = defragmented_disk[cur_index]
            cur_size = id_to_space[cur_id]
            cur_start_pos = id_to_start_pos[cur_id]
            for free_start_pos, free_space in sorted(pos_to_free_space.items()):
                if free_start_pos < cur_start_pos and cur_size <= free_space:
                    for i in range(cur_size):
                        defragmented_disk[free_start_pos+i] = defragmented_disk[cur_start_pos+i]
                        defragmented_disk[cur_start_pos+i] = None
                    pos_to_free_space.pop(free_start_pos)
                    if cur_size < free_space:
                        pos_to_free_space[free_start_pos+cur_size] = free_space - cur_size
                    id_to_start_pos[cur_id] = free_start_pos
                    break
            else:
                cur_index = cur_start_pos - 1

    print('|'.join([str(elem) if elem is not None else '.' for elem in defragmented_disk]))
    check_sum = 0
    for position, file_id in enumerate(defragmented_disk):
        if file_id is not None:
            check_sum += position * file_id

    print(check_sum)


if __name__ == '__main__':
    main()