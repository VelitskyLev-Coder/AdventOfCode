import copy


class LavaMap:
    def __init__(self, lava_map: list[str]):
        self.lava_map = copy.deepcopy(lava_map)

    def _transpose_map(self):
        new_map = [''.join(column) for column in zip(*self.lava_map)]
        self.lava_map = new_map

    def get_horizontal_reflection_indexes(self) -> list[int]:
        return [i for i in range(1, len(self.lava_map) + 1) if self.is_row_reflection(i)]

    def get_vertical_reflection_indexes(self) -> list[int]:
        self._transpose_map()
        result = self.get_horizontal_reflection_indexes()
        self._transpose_map()
        return result

    def get_horizontal_reflection_lines_fixed(self) -> tuple[int]:
        reg_hor_ref_lines = tuple(self.get_horizontal_reflection_indexes())
        for i in range(len(self.lava_map)):
            for j in range(len(self.lava_map[0])):
                swap_dict = {'.': '#', '#': '.'}
                self.lava_map[i] = f"{self.lava_map[i][:j]}{swap_dict[self.lava_map[i][j]]}{self.lava_map[i][j+1:]}"
                new_ref_lines = tuple(self.get_horizontal_reflection_indexes())
                self.lava_map[i] = f"{self.lava_map[i][:j]}{swap_dict[self.lava_map[i][j]]}{self.lava_map[i][j+1:]}"
                if new_ref_lines and new_ref_lines != reg_hor_ref_lines:
                    return tuple(set(new_ref_lines).difference(set(reg_hor_ref_lines)))
        return tuple()

    def get_vertical_reflection_lines_fixed(self) -> tuple:
        self._transpose_map()
        result = self.get_horizontal_reflection_lines_fixed()
        self._transpose_map()
        return result

    def is_row_reflection(self, row_index: int) -> bool:
        if row_index == len(self.lava_map):
            return False
        for row1, row2 in zip(self.lava_map[row_index - 1::-1], self.lava_map[row_index:]):
            if row1 != row2:
                return False
        return True
