from sequence import Sequence
from solution_part1 import get_input


def main():
    input_data = get_input()
    sequences = [Sequence(number_list) for number_list in input_data]
    for sequence in sequences:
        sequence.interpolate_one_backward()
    print(sum(sequence.get_first() for sequence in sequences))


if __name__ == '__main__':
    main()
