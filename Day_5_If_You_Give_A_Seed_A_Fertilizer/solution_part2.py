from typing import Iterable, Union, Optional

from solution_part1 import get_input as get_input_part1, OneToOtherMap, RangeMap, MapComposition


class Range:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __contains__(self, value):
        return self.min_value <= value <= self.max_value

    def __repr__(self):
        return f'[{self.min_value}, {self.max_value}]'

    def get_out_in_out(self, min_value, max_value) -> tuple[Optional['Range'], Optional['Range'], Optional['Range']]:
        outside_left, inside, outside_right = None, None, None

        # Check for left range (outside_left)
        if self.min_value < min_value:
            left_end = min(min_value - 1, self.max_value)
            outside_left = Range(self.min_value, left_end)

        # Check for middle range (inside)
        if not (max_value < self.min_value or min_value > self.max_value):
            inside_start = max(self.min_value, min_value)
            inside_end = min(self.max_value, max_value)
            inside = Range(inside_start, inside_end)

        # Check for right range (outside_right)
        if self.max_value > max_value:
            right_start = max(self.min_value, max_value + 1)
            outside_right = Range(right_start, self.max_value)

        return outside_left, inside, outside_right


class OneToOtherMapRanges(OneToOtherMap):
    def __init__(self, from_name: str, to_name: str, range_maps: Iterable[RangeMap]):
        super().__init__(from_name, to_name, range_maps)

    def get_mapped_value(self, range_arg: Union[list[Range], Range]) -> list[Range]:
        if isinstance(range_arg, Range):
            range_arg = [range_arg]
        range_arg = list(range_arg)

        result = []
        for range_map in self.range_maps:
            new_ranges = []
            for single_range in range_arg:
                left, middle, right = single_range.get_out_in_out(range_map.min_arg(), range_map.max_arg())
                if left is not None:
                    new_ranges.append(left)
                if right is not None:
                    new_ranges.append(right)
                if middle is not None:
                    result.append(Range(min_value=range_map.get_mapped_value(middle.min_value),
                                        max_value=range_map.get_mapped_value(middle.max_value)))
            range_arg = list(new_ranges)
            new_ranges.clear()
        result.extend(range_arg)
        return result


def find_min_location(seeds: list[Range], all_maps: list[OneToOtherMapRanges]):
    multi_map = MapComposition.from_many_one_to_other_maps(all_maps)
    # noinspection PyTypeChecker
    result_ranges = multi_map.get_mapped_value(seeds)
    min_values = [r.min_value for r in result_ranges]
    return min(min_values)


def get_input() -> tuple[list[Range], list[OneToOtherMapRanges]]:
    seeds_pairs, maps = get_input_part1()
    seeds = list()
    for start_number, range_length in zip(seeds_pairs[::2], seeds_pairs[1::2]):
        seeds.append(Range(start_number, start_number+range_length-1))
    maps = [OneToOtherMapRanges(old_map.from_name, old_map.to_name, old_map.range_maps) for old_map in maps]
    return seeds, maps


def main():
    print(find_min_location(*get_input()))


if __name__ == '__main__':
    main()
