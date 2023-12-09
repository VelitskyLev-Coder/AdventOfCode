from sequence import Sequence


def get_input() -> list[list[int]]:
    sequences = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            if not line.strip():
                continue
            sequences.append(list(map(int, line.split())))
    return sequences


def main():
    input_data = get_input()
    sequences = [Sequence(number_list) for number_list in input_data]
    for sequence in sequences:
        sequence.interpolate_one_forward()
    print(sum(sequence.get_last() for sequence in sequences))


if __name__ == '__main__':
    main()
