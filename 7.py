from functools import cmp_to_key

with open("input/7.txt", "r") as f:
    lines = f.readlines()

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

def score_hand(hand : str):
    values = [card_values[card] for card in hand]
    counts = [values.count(card_value) for card_value in set(values)]

    # five of a kind
    if 5 in counts:
        return 9, values
    # four of a kind
    if 4 in counts:
        return 8, values
    # full house
    if 3 in counts and 2 in counts:
        return 7, values
    # three of a kind
    if 3 in counts:
        return 6, values
    # two pair
    if counts.count(2) == 2:
        return 5, values
    # pair
    if 2 in counts:
        return 4, values
    # high card
    return 0, values

hands = [line.split()[0] for line in lines]
bids = [int(line.split()[1]) for line in lines]

bid_scores = [(score_hand(hand), bid) for hand, bid in zip(hands, bids)]

def compare_bid_score(a, b):
    a_score, a_bid = a
    b_score, b_bid = b
    a_type, a_values = a_score
    b_type, b_values = b_score
    if a_type > b_type:
        return 1
    if a_type < b_type:
        return -1
    for a_value, b_value in zip(a_values, b_values):
        if a_value > b_value:
            return 1
        if a_value < b_value:
            return -1
    return 0

sorted_bid_scores = sorted(bid_scores, key=cmp_to_key(compare_bid_score))
winnings = [((i + 1), bid_score[1]) for i, bid_score in enumerate(sorted_bid_scores)]
total_winnings = sum([a * b for a, b in winnings])

print(total_winnings)

# part 2

card_values["J"] = 0

def convert_jokers(hand):
    counts = [hand.count(card) for card in hand]
    max_count = max(counts)
    cards_with_max_count = [card for card, count in zip(hand, counts) if count == max_count]
    highest_card = sorted(cards_with_max_count, key=lambda card: card_values[card])[-1]
    return hand.replace("J", highest_card)

hands = [line.split()[0] for line in lines]
bids = [int(line.split()[1]) for line in lines]

def compare_hands(a, b):
    a_cards, a_bid = a
    b_cards, b_bid = b
    a_converted = convert_jokers(a_cards)
    b_converted = convert_jokers(b_cards)
    a_score, _ = score_hand(a_converted)
    b_score, _ = score_hand(b_converted)
    if a_score > b_score:
        return 1
    if a_score < b_score:
        return -1
    a_values = [card_values[card] for card in a_cards]
    b_values = [card_values[card] for card in b_cards]
    for a_value, b_value in zip(a_values, b_values):
        if a_value > b_value:
            return 1
        if a_value < b_value:
            return -1
    return 0

hand_bids = [(hand, bid) for hand, bid in zip(hands, bids)]
sorted_hand_bids = sorted(hand_bids, key=cmp_to_key(compare_hands))

print(sorted_hand_bids)

winnings = [((i + 1), bid_score[1]) for i, bid_score in enumerate(sorted_hand_bids)]
total_winnings = sum([a * b for a, b in winnings])

print(total_winnings)