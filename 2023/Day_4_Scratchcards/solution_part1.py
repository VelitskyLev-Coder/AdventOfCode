from typing import Iterable


class Card:
    def __init__(self, card_id: int, winning_numbers: Iterable[int], card_numbers: Iterable[int]):
        self.card_id = card_id
        self.winning_numbers = list(winning_numbers)
        self.card_numbers = list(card_numbers)

    def __repr__(self):
        return (f'Card {self.card_id}: '
                f'{" ".join(map(str, self.winning_numbers))} | {" ".join(map(str, self.card_numbers))}')

    def get_actual_winning_numbers(self) -> list[int]:
        return [n for n in self.card_numbers if n in self.winning_numbers]

    def get_score(self):
        actual_winning_numbers = self.get_actual_winning_numbers()
        if not actual_winning_numbers:
            return 0
        return 2**(len(actual_winning_numbers)-1)


def main():
    all_cards = get_input()
    print(sum(card.get_score() for card in all_cards))


def get_input() -> list[Card]:
    result_list = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram.readlines():
            case, numbers = line.strip().split(':')
            card_id = int(case.strip().split()[1])
            win_numbers_str, card_numbers_str = numbers.split('|')
            result_list.append(
                Card(card_id=card_id,
                     winning_numbers=map(int, win_numbers_str.strip().split()),
                     card_numbers=map(int, card_numbers_str.strip().split()))
            )
    return result_list


if __name__ == '__main__':
    main()
