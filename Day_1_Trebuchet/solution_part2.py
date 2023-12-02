from typing import Iterable
from solution_part1 import get_input
import re


def main():
    print(sum(list(map(get_calibration_value, get_input()))))


def get_calibration_value(input_string: str) -> int:
    token_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    token_dict.update({
        (str(d), d) for d in range(10)
    })

    pattern = '(?=(' + '|'.join(token_dict.keys()) + '))'
    all_digits = [token_dict[t] for t in re.findall(pattern, input_string)]
    if not all_digits:
        raise ValueError(f'{input_string} must contain at least one digit')
    return all_digits[0] * 10 + all_digits[-1]


if __name__ == '__main__':
    main()
