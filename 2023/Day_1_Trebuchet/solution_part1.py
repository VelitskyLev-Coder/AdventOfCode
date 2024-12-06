from typing import Iterable


def main():
    print(sum(list(map(get_calibration_value, get_input()))))


def get_input() -> Iterable[str]:
    with open('input_1.txt') as input_stram:
        return (line.strip() for line in input_stram.readlines())


def get_calibration_value(input_string: str) -> int:
    all_digits = [int(ch) for ch in input_string if ch.isdigit()]
    if not all_digits:
        raise ValueError(f'{input_string} must contain at least one digit')
    return all_digits[0] * 10 + all_digits[-1]


if __name__ == '__main__':
    main()
