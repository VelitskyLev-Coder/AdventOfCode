from typing import Iterable


def get_input() -> tuple[list[int], list[int]]:
    with open('input_1.txt') as input_stram:
        time_line = input_stram.readline()
        distance_line = input_stram.readline()

    times = list(map(int, time_line.removeprefix('Time:').split()))
    distances = list(map(int, distance_line.removeprefix('Distance:').split()))

    return times, distances


def get_distances(total_time: int) -> Iterable[int]:
    return (t*(total_time - t) for t in range(total_time+1))


def main():
    result = 1
    for time, distance in zip(*get_input()):
        result *= sum(1 for d in get_distances(time) if d > distance)
    print(result)


if __name__ == '__main__':
    main()
