import re
from typing import Iterable


class OutOfRangeException(Exception):
    pass


class RangeMap:
    def __init__(self, dest_range_start: int, source_range_start: int, range_length: int):
        self.dest_range_start = dest_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

    def min_arg(self) -> int:
        return self.source_range_start

    def max_arg(self) -> int:
        return self.source_range_start + self.range_length - 1

    def get_mapped_value(self, arg: int):
        if arg < self.min_arg() or arg > self.max_arg():
            raise OutOfRangeException(f'{arg} is out of range. '
                                      f'Min_value = {self.min_arg()}. Max_value = {self.max_arg()}')
        offset = arg - self.source_range_start
        return self.dest_range_start + offset

    @staticmethod
    def from_text_line(text_line: str) -> 'RangeMap':
        dest_range_start, source_range_start, range_length = map(int, text_line.split())
        return RangeMap(dest_range_start, source_range_start, range_length)


class OneToOtherMap:
    def __init__(self, from_name: str, to_name: str, range_maps: Iterable[RangeMap]):
        self.from_name = from_name
        self.to_name = to_name
        self.range_maps: list[RangeMap] = list(range_maps)

    def get_mapped_value(self, arg: int):
        for range_map in self.range_maps:
            try:
                return range_map.get_mapped_value(arg)
            except OutOfRangeException as _:
                continue
        return arg

    @staticmethod
    def from_text_block(text_block: str) -> 'OneToOtherMap':
        all_lines = text_block.splitlines()
        all_lines_it = (line for line in all_lines if line.strip())
        name_line = next(all_lines_it)
        names = name_line.split()[0]
        from_name, to_name = names.split('-to-')
        all_range_maps = (RangeMap.from_text_line(line) for line in all_lines_it)
        return OneToOtherMap(from_name, to_name, all_range_maps)


class MapComposition(OneToOtherMap):
    def __init__(self, first_map: OneToOtherMap, second_map: OneToOtherMap):
        if second_map.from_name != first_map.to_name:
            raise ValueError(f'Composition Error!')
        super().__init__(first_map.from_name, second_map.to_name, range_maps=[])
        self.first_map = first_map
        self.second_map = second_map

    def get_mapped_value(self, arg):
        return self.second_map.get_mapped_value(self.first_map.get_mapped_value(arg))

    @staticmethod
    def from_many_one_to_other_maps(one_to_other_maps: Iterable[OneToOtherMap]) -> 'MapComposition':
        one_to_other_maps = list(one_to_other_maps)
        multi_map = one_to_other_maps[0]
        for one_to_other_map in one_to_other_maps[1:]:
            multi_map = MapComposition(multi_map, one_to_other_map)
        return multi_map


def find_min_location(seeds: list[int], all_maps: list[OneToOtherMap]):
    multi_map = MapComposition.from_many_one_to_other_maps(all_maps)
    min_seed = min(seeds, key=lambda seed_id: multi_map.get_mapped_value(seed_id))
    return multi_map.get_mapped_value(min_seed)


def main():
    print(find_min_location(*get_input()))


def get_input() -> tuple[list[int], list[OneToOtherMap]]:
    one_to_other_maps_list = list()
    seeds = list()

    with open('input_1.txt') as input_stram:
        accumulated_block = None
        for line in input_stram.readlines():
            if line.startswith('seeds:'):
                seeds = list(map(int, line.removeprefix('seeds: ').split()))
            if re.match(r'[a-z]+-to-[a-z]+ map:', line):
                accumulated_block = line
                continue
            if not line.strip() and accumulated_block:
                one_to_other_maps_list.append(OneToOtherMap.from_text_block(accumulated_block))
                accumulated_block = None
                continue
            if accumulated_block:
                accumulated_block += line

        if accumulated_block:
            one_to_other_maps_list.append(OneToOtherMap.from_text_block(accumulated_block))

        return seeds, one_to_other_maps_list


if __name__ == '__main__':
    main()
