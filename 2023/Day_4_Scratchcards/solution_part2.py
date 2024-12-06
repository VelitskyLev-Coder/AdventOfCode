from solution_part1 import get_input


def main():
    all_cards = sorted(get_input(), key=lambda card: card.card_id)
    all_card_ids = [card.card_id for card in all_cards]
    card_by_id = {card.card_id: card for card in all_cards}
    card_count_by_id = {card.card_id: 1 for card in all_cards}

    for card_id in all_card_ids:
        win_cards = len(card_by_id[card_id].get_actual_winning_numbers())
        for i in range(card_id + 1, card_id + win_cards + 1):
            card_count_by_id[i] += card_count_by_id[card_id]

    print(sum(card_count_by_id.values()))


if __name__ == '__main__':
    main()
