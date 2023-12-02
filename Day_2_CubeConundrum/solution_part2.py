import operator
from solution_part1 import Game, Round, get_input
import functools


def main():
    all_games = get_input()
    print(sum(map(calculate_power, all_games)))


def calculate_power(game_round: Game) -> int:
    def reduce_rounds(round1: Round, round2: Round):
        return Round(
            red=max(round1.red, round2.red),
            green=max(round1.green, round2.green),
            blue=max(round1.blue, round2.blue),
        )

    maximal_round = functools.reduce(reduce_rounds, game_round.rounds)
    return functools.reduce(operator.mul, maximal_round)


if __name__ == '__main__':
    main()
