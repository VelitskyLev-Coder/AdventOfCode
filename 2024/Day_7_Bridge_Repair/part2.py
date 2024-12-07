import itertools
from typing import NamedTuple
import operator

from tqdm import tqdm


class CalibrationRecord(NamedTuple):
    result: int
    numbers: tuple[int, ...]

def concat_operator(n1: int, n2: int) -> int:
    return int(str(n1)+str(n2))

def could_be_valid(record: CalibrationRecord):
    for operators in itertools.product((operator.add, operator.mul, concat_operator), repeat=len(record.numbers)-1):
        cur_value = record.numbers[0]
        for cur_operator, rhs in zip(operators, itertools.islice(record.numbers, 1, None)):
            cur_value = cur_operator(cur_value, rhs)
        if cur_value == record.result:
            return True

    return False

def main():
    calibrations = list()
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                result_str, numbers_str = line.split(':')
                calibrations.append(CalibrationRecord(int(result_str), tuple(map(int, numbers_str.split()))))

    result = 0
    for record in tqdm(calibrations):
        if could_be_valid(record):
            result += record.result

    print(result)

if __name__ == '__main__':
    main()