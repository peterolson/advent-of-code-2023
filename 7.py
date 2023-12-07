from functools import cmp_to_key

with open("input/7.txt", "r") as f:
    lines = f.readlines()

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

hands = [line.split()[0] for line in lines]
bids = [int(line.split()[1]) for line in lines]

def compare_bid_score(a, b):
    a_hand, a_bid = a
    b_hand, b_bid = b
    counts_a = sorted([a_hand.count(card) for card in set(a_hand)], reverse=True)
    counts_b = sorted([b_hand.count(card) for card in set(b_hand)], reverse=True)
    for count_a, count_b in zip(counts_a, counts_b):
        if count_a > count_b:
            return 1
        if count_a < count_b:
            return -1
    for a_value, b_value in zip(a_hand, b_hand):
        if card_values[a_value] > card_values[b_value]:
            return 1
        if card_values[a_value] < card_values[b_value]:
            return -1
    return 0

hand_bids = [(hand, bid) for hand, bid in zip(hands, bids)]
sorted_hand_bids = sorted(hand_bids, key=cmp_to_key(compare_bid_score))
winnings = [((i + 1), bid_score[1]) for i, bid_score in enumerate(sorted_hand_bids)]
total_winnings = sum([a * b for a, b in winnings])

print(f"Part 1: {total_winnings}")

# part 2

card_values["J"] = 0

def convert_jokers(hand):
    non_jokers = hand.replace("J", "")
    if len(non_jokers) == 0:
        return hand
    most_common_card = max(set(non_jokers), key=hand.count)
    return hand.replace("J", most_common_card)

hands = [line.split()[0] for line in lines]
bids = [int(line.split()[1]) for line in lines]

def compare_hands(a, b):
    a_cards, a_bid = a
    b_cards, b_bid = b
    a_converted = convert_jokers(a_cards)
    b_converted = convert_jokers(b_cards)
    
    counts_a = sorted([a_converted.count(card) for card in set(a_converted)], reverse=True)
    counts_b = sorted([b_converted.count(card) for card in set(b_converted)], reverse=True)
    for count_a, count_b in zip(counts_a, counts_b):
        if count_a > count_b:
            return 1
        if count_a < count_b:
            return -1
    
    for a_card, b_card in zip(a_cards, b_cards):
        if card_values[a_card] > card_values[b_card]:
            return 1
        if card_values[a_card] < card_values[b_card]:
            return -1
    return 0

hand_bids = [(hand, bid) for hand, bid in zip(hands, bids)]
sorted_hand_bids = sorted(hand_bids, key=cmp_to_key(compare_hands))

winnings = [((i + 1), bid_score[1]) for i, bid_score in enumerate(sorted_hand_bids)]
total_winnings = sum([a * b for a, b in winnings])

print(f"Part 2: {total_winnings}")