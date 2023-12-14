
class DishMap:
    def __init__(self, dish_map: list[str]):
        self.dish_map = [list(line) for line in dish_map]

    def _rotate_clockwise(self):
        self.dish_map = [list(column)[::-1] for column in zip(*self.dish_map)]

    def perform_cycle(self):
        self.shift_all_top()
        self._rotate_clockwise()
        self.shift_all_top()
        self._rotate_clockwise()
        self.shift_all_top()
        self._rotate_clockwise()
        self.shift_all_top()
        self._rotate_clockwise()

    def print_map(self):
        print('*' * 25)
        for line in self.dish_map:
            print(''.join(line))

    def get_as_long_string(self) -> str:
        return ''.join((''.join(line) for line in self.dish_map))

    def _shift_all_one_north(self):
        for i in range(len(self.dish_map)):
            self._shift_line_one_north(i)

    def _shift_line_one_north(self, index: int):
        if index == 0:
            return
        for i in range(len(self.dish_map[index])):
            if self.dish_map[index][i] == 'O' and self.dish_map[index - 1][i] == '.':
                self.dish_map[index - 1][i] = 'O'
                self.dish_map[index][i] = '.'

    def shift_all_top(self):
        for _ in range(len(self.dish_map)):
            self._shift_all_one_north()

    def calculate_cost(self):
        total_load = 0
        for i, row in enumerate(self.dish_map):
            for ch in row:
                if ch == 'O':
                    total_load += len(self.dish_map) - i

        return total_load
