import copy
import itertools
from typing import NamedTuple


class Universe:
    def __init__(self, universe_map: list[list[str]]):
        self.universe_map = copy.deepcopy(universe_map)

    def _expand_rows(self):
        def expand_generator(universe_map: list[list[str]]):
            universe_map_copy = copy.deepcopy(universe_map)
            for row in universe_map_copy:
                yield row
                if all(ch == '.' for ch in row):
                    yield row

        self.universe_map = list(expand_generator(self.universe_map))

    def _transpose_map(self):
        new_map = [list(column) for column in zip(*self.universe_map)]
        self.universe_map = new_map

    def expand_universe(self):
        self._expand_rows()
        self._transpose_map()
        self._expand_rows()
        self._transpose_map()

    def get_paths_sum(self) -> int:
        class Cord(NamedTuple):
            y: int
            x: int

        path_coordinate_list = list()
        for i, row in enumerate(self.universe_map):
            for j, ch in enumerate(row):
                if ch == '#':
                    path_coordinate_list.append(Cord(i, j))

        paths_sum = 0
        for cord1, cord2 in itertools.combinations(path_coordinate_list, 2):
            distance = abs(cord1.x - cord2.x) + abs(cord1.y - cord2.y)
            paths_sum += distance

        return paths_sum


def get_input() -> list[list[str]]:
    result = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            if not line.strip():
                continue
            result.append(list(line.strip()))
    return result


def main():
    universe = Universe(get_input())
    universe.expand_universe()
    print(universe.get_paths_sum())


if __name__ == '__main__':
    main()
