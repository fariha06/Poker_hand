def rank_hands(hand1, hand2):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def parse_hand(hand):
        values_list = [values[card] for card in hand]
        counts = {card: hand.count(card) for card in hand}
        values_list.sort(reverse=True)
        return values_list, counts

    def check_hand_type(counts, n):
        return [value for value, count in counts.items() if count == n]

    def compare_hands(hand1_values, hand2_values):
        for card1, card2 in zip(hand1_values, hand2_values):
            if card1 > card2:
                return "First hand wins!"
            elif card1 < card2:
                return "Second hand wins!"
        return "It's a tie!"

    hand1_values, hand1_counts = parse_hand(hand1)
    hand2_values, hand2_counts = parse_hand(hand2)

    for n in [4, 3, 2]:
        hand1_type = check_hand_type(hand1_counts, n)
        hand2_type = check_hand_type(hand2_counts, n)

        if len(hand1_type) > 0 and len(hand2_type) == 0:
            return "First hand wins!"
        elif len(hand1_type) == 0 and len(hand2_type) > 0:
            return "Second hand wins!"
        elif len(hand1_type) > 0 and len(hand2_type) > 0:
            if values[hand1_type[0]] > values[hand2_type[0]]:
                return "First hand wins!"
            elif values[hand1_type[0]] < values[hand2_type[0]]:
                return "Second hand wins!"

    return compare_hands(hand1_values, hand2_values)


# Test cases
print(rank_hands("KQ23Q", "TA3J7"))  # First hand wins!
print(rank_hands("KTQTT", "AAQQT"))  # First hand wins!
print(rank_hands("AKKAA", "222T2"))  # Second hand wins!
print(rank_hands("A3A46", "K32KT"))  # First hand wins!
print(rank_hands("A3A46", "258AA"))  # Second hand wins!
print(rank_hands("TA982", "98TA2"))  # It's a tie!
print(rank_hands("32233", "A4A5A"))  # First hand wins!
