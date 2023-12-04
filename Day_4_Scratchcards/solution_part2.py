from solution_part1 import get_input


def main():
    all_cards = get_input()
    card_by_id = {card.card_id: card for card in all_cards}
    result_cards_count = 0

    while all_cards:
        cur_card = all_cards.pop()
        for i in range(cur_card.card_id + 1, cur_card.card_id + len(cur_card.get_actual_winning_numbers()) + 1):
            all_cards.append(card_by_id[i])
        result_cards_count += 1
    print(result_cards_count)


if __name__ == '__main__':
    main()
