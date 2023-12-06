from solution_part1 import get_input as get_input_part_1, get_distances


def get_input() -> tuple[int, int]:
    times, distances = get_input_part_1()
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))
    return time, distance


def main():
    time, distance = get_input()
    print(sum(1 for d in get_distances(time) if d > distance))


if __name__ == '__main__':
    main()
