from collections import Counter


class Card():

    def __init__(self, input):
        number = input[0:-1]
        if number == "A":
            self.number = 14
        elif number == "K":
            self.number = 13
        elif number == "Q":
            self.number = 12
        elif number == "J":
            self.number = 11
        else:
            self.number = int(number)
        self.suit = input[-1]


def checkNumbers(cards):
    nums = []
    for card in cards:
        nums.append(card.number)
    nums = dict(Counter(nums).items())
    pairs = 0
    threes = 0
    for key in nums:
        if nums[key] == 2:
            pairs += 1
        elif nums[key] == 3:
            threes += 1
        elif nums[key] == 4:
            return "Four of a kind"
        else:
            pass
    if pairs == 1 and threes == 1:
        return "Full house"
    elif threes == 1:
        return "Three of a kind"
    elif pairs > 0:
        return "{} pair".format(pairs)
    else:
        return


def checkFlush(cards):
    suit = cards[0].suit
    for card in cards:
        if card.suit != suit:
            return False
    return True


def checkStraight(cards):
    nums = []
    for card in cards:
        nums.append(card.number)
    nums.sort()
    straight = True
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            straight = False
            break
    return straight


def main():
    example_hand = "AS, 10C, 10H, 3D, 3S"
    hand = example_hand.split(", ")
    cards = []
    for card in hand:
        cards.append(Card(card))
    for card in cards:
        print("{} of {}".format(card.number, card.suit))
    flush = checkFlush(cards)
    if flush:
        print("Flush")
    straight = checkStraight(cards)
    if straight:
        print("Straight")
    nums = checkNumbers(cards)
    if nums:
        print(nums)
    else:
        print("No combos")


main()
