from collections import defaultdict
from typing import NamedTuple


class Round(NamedTuple):
    red: int
    green: int
    blue: int


class Game:
    def __init__(self, game_id: int):
        self.game_id = game_id
        self.rounds: list[Round] = list()

    def add_round(self, game_round: Round):
        self.rounds.append(game_round)

    def __repr__(self):
        return f'Game {self.game_id}: {self.rounds}'


def main():
    all_games = get_input()
    possible_games = filter(lambda game: all((possible_round(r) for r in game.rounds)), all_games)
    print(sum(game.game_id for game in possible_games))


def possible_round(game_round: Round) -> bool:
    return game_round.red <= 12 and game_round.green <= 13 and game_round.blue <= 14


def get_input() -> list[Game]:
    game_list = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram.readlines():
            game, rounds = line.split(':')
            _, game_id_str = game.split(' ')
            game_id = int(game_id_str)
            cur_game = Game(game_id)
            for round_record in rounds.split(';'):
                count_dict = defaultdict(lambda: 0)
                for color_record in round_record.split(','):
                    count_str, color = color_record.strip().split(' ')
                    count_dict[color.strip()] += int(count_str)
                cur_game.add_round(Round(
                    red=count_dict.get('red', 0),
                    green=count_dict.get('green', 0),
                    blue=count_dict.get('blue', 0),
                ))
            game_list.append(cur_game)
    return game_list


if __name__ == '__main__':
    main()
