from typing import NamedTuple


class Board:
    def __init__(self, board_matrix: list[list[str]]):
        self.board = board_matrix

    def get_max_x(self):
        return len(self.board[0]) - 1

    def get_max_y(self):
        return len(self.board) - 1

    def get_all_numbers(self) -> list['NumberOnBoard']:
        number_on_board_list = list()
        x_left = None
        x_right = None
        for y, line in enumerate(self.board):
            cur_number_str = ''
            for x, ch in enumerate(line):
                if ch.isdigit():
                    cur_number_str += ch
                    if x_left is None:
                        x_left = x
                    x_right = x
                if (not ch.isdigit() or x == self.get_max_x()) and cur_number_str:
                    number_on_board_list.append(NumberOnBoard(
                        board=self,
                        number=int(cur_number_str),
                        y=y,
                        x_left=x_left,
                        x_right=x_right
                    ))
                    x_left = None
                    x_right = None
                    cur_number_str = ''
        return number_on_board_list

    def is_inside(self, point: 'GridPoint') -> bool:
        return 0 <= point.x <= self.get_max_x() and 0 <= point.y <= self.get_max_y()

    def get_ch_by_point(self, point: 'GridPoint'):
        return self.board[point.y][point.x]


class GridPoint(NamedTuple):
    x: int
    y: int


class NumberOnBoard:
    def __init__(self, board: Board, number: int, y, x_left, x_right):
        self.board = board
        self.number = number
        self.y = y
        self.x_left = x_left
        self.x_right = x_right

    def get_all_neighbours_chars(self) -> list[str]:
        return [self.board.get_ch_by_point(point) for point in self.get_all_neighbours()]

    def get_all_neighbours(self) -> list[GridPoint]:
        neighbours = list()
        for y in range(self.y - 1, self.y + 2):
            for x in range(self.x_left - 1, self.x_right + 2):
                if y == self.y and self.x_left <= x <= self.x_right:
                    continue
                if self.board.is_inside(GridPoint(x, y)):
                    ch = self.board.get_ch_by_point(GridPoint(x, y))
                    if ch != '.' and not ch.isdigit():
                        neighbours.append(GridPoint(x, y))
        return neighbours

    def __repr__(self):
        return f'(number = {self.number}, y = {self.y}, x_left = {self.x_left}, x_right = {self.x_right})'


def main():
    board = Board(get_input())
    all_numbers_on_board = board.get_all_numbers()
    print(sum(number.number for number in all_numbers_on_board if number.get_all_neighbours_chars()))


def get_input() -> list[list[str]]:
    result_list = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram.readlines():
            result_list.append(list(line.strip()))
    return result_list


if __name__ == '__main__':
    main()
