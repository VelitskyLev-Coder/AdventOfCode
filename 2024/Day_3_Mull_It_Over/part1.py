import re

def calc_part_1(memory: str) -> int:
    pattern = re.compile(r'mul\((?P<lhs>\d+),(?P<rhs>\d+)\)')
    result = 0
    for match in re.finditer(pattern, memory):
        result += int(match.group('lhs')) * int(match.group('rhs'))
    return result

def main():
    with open('input.txt') as input_file:
        memory = input_file.read().strip()

    print(calc_part_1(memory))


if __name__ == '__main__':
    main()