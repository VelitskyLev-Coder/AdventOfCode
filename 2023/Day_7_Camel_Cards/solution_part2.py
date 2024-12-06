import itertools
from solution_part1 import get_input, Card, Hand, HandAndBid


class WildCard(Card):
    # noinspection SpellCheckingInspection
    _values_in_order = list('AKQT98765432J')

    @classmethod
    def get_values_in_order(cls):
        return cls._values_in_order


class WildHand(Hand):
    card_factory = WildCard

    def __init__(self, hand_line: str):
        super().__init__(hand_line)
        self.type = self._determine_type()

    def _determine_type(self) -> 'Hand.Type':
        joker_indices = [index for index, card in enumerate(self.cards) if card.ch == 'J']

        all_possible_hands = list()
        if not joker_indices:
            all_possible_hands.append(''.join([card.ch for card in self.cards]))
        else:
            for replace_tuple in itertools.product(*([list(WildCard.get_values_in_order())]*len(joker_indices))):
                new_hand = [card.ch for card in self.cards]
                for index, replacer in zip(joker_indices, replace_tuple):
                    new_hand[index] = replacer
                all_possible_hands.append(''.join(new_hand))

        return max(Hand(hand_str).type for hand_str in all_possible_hands)

    def __repr__(self):
        return super().__repr__()


def main():
    hand_and_bid_list = [HandAndBid(WildHand(hand_str), bid) for hand_str, bid in zip(*get_input())]
    hand_and_bid_list_sorted = list(sorted(hand_and_bid_list, key=lambda hand_and_bid: hand_and_bid.hand))
    print(hand_and_bid_list_sorted)
    print(sum(hand_and_bid.bid * place for place, hand_and_bid in enumerate(hand_and_bid_list_sorted, start=1)))
    pass


if __name__ == '__main__':
    main()
