from enum import IntEnum
from collections import Counter
from typing import NamedTuple


class Card:
    # noinspection SpellCheckingInspection
    _values_in_order = list('AKQJT98765432')

    def __init__(self, ch: str):
        if ch not in self._values_in_order:
            raise ValueError(f'Card may be one of {self._values_in_order}, but {ch} was given')
        self.ch = ch
        self.power = len(self._values_in_order) - self._values_in_order.index(ch) - 1

    def __eq__(self, other):
        return self.ch == other.ch

    def __lt__(self, other):
        return self.power < other.power

    def __hash__(self):
        return self.power

    def __repr__(self):
        return self.ch


class Hand:
    card_factory = Card

    class Type(IntEnum):
        HIGH_CARD = 0
        ONE_PAIR = 1
        TWO_PAIR = 2
        THREE_OF_A_KIND = 3
        FULL_HOUSE = 4
        FOUR_OF_A_KIND = 5
        FIVE_OF_A_KIND = 6

    def __init__(self, hand_line: str):
        self.cards = [self.card_factory(ch) for ch in hand_line.strip()]
        self.type = self._determine_type()

    def _determine_type(self) -> 'Hand.Type':
        count_arr = Counter(self.cards)
        if len(count_arr) == 5:
            return Hand.Type.HIGH_CARD
        if len(count_arr) == 4:
            return Hand.Type.ONE_PAIR
        if len(count_arr) == 3:
            if 3 in count_arr.values():
                return Hand.Type.THREE_OF_A_KIND
            else:
                return Hand.Type.TWO_PAIR
        if len(count_arr) == 2:
            if 4 in count_arr.values():
                return Hand.Type.FOUR_OF_A_KIND
            else:
                return Hand.Type.FULL_HOUSE
        return Hand.Type.FIVE_OF_A_KIND

    def __repr__(self):
        return f"{''.join(map(str, self.cards))}, type = {self.type}"

    def __lt__(self, other: 'Hand'):
        if self.type != other.type:
            return self.type < other.type
        for card_from_this_hand, card_from_other_hand in zip(self.cards, other.cards):
            if card_from_this_hand < card_from_other_hand:
                return True
            elif card_from_this_hand > card_from_other_hand:
                return False
        return False


def get_input() -> tuple[list[str], list[int]]:
    hands = list()
    bids = list()
    with open('input_1.txt') as input_stram:
        for line in input_stram:
            hand_str, bid_str = line.split()
            hands.append(hand_str)
            bids.append(int(bid_str))
    return hands, bids


class HandAndBid(NamedTuple):
    hand: Hand
    bid: int


def main():
    hand_and_bid_list = [HandAndBid(Hand(hand_str), bid) for hand_str, bid in zip(*get_input())]
    hand_and_bid_list_sorted = list(sorted(hand_and_bid_list, key=lambda hand_and_bid: hand_and_bid.hand))
    print(sum(hand_and_bid.bid * place for place, hand_and_bid in enumerate(hand_and_bid_list_sorted, start=1)))


if __name__ == '__main__':
    main()
