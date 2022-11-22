from collections import Counter
import random


class Card():

    def __init__(self, input=None):
        if input:
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

    def __str__(self):
        if self.number == 14:
            number = "A"
        if self.number == 13:
            number = "K"
        if self.number == 12:
            number = "Q"
        if self.number == 11:
            number = "J"
        else:
            number = str(self.number)
        return number + self.suit

    def random(self):
        self.number = random.choice(list(range(2, 11)) + ['J', 'Q', 'K', 'A'])
        self.suit = random.choice(['S', 'H', 'C', 'D'])
        return self


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


def evalHand(hand):
    hand = hand.split(", ")
    cards = []
    for card in hand:
        cards.append(Card(card))
    flush = checkFlush(cards)
    straight = checkStraight(cards)
    nums = checkNumbers(cards)
    if flush and straight:
        return "Straight flush"
    elif nums and "Four" in nums:
        return nums
    elif nums and "Full" in nums:
        return nums
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif nums:
        return nums
    else:
        return "No combos"


def demo():
    test_hands = [
        "AS, 10C, 10H, 3D, 3S",
        "AS, 10C, JH, KD, QS",
        "AS, 10S, JS, KS, QS",
        "AS, 10C, 10H, 10D, 10S",
        "10S, 10C, 10H, 3D, 3S",
    ]
    for hand in test_hands:
        print(hand)
        print(evalHand(hand))


def shuffle():
    cards = []
    hand = []
    while len(cards) < 5:
        card = Card().random()
        if str(card) not in cards:
            cards.append(str(card))
    # for card in cards:
    #     hand.append(str(card))
    hand = ", ".join(cards)
    print(hand)
    print(evalHand(hand))


def main():
    print("You can run a demo of test hands, shuffle the deck for a random hand, or enter your own hand.")
    while(True):
        response = input(
            "Enter D for demo, S for shuffle, your custom hand of 5 cards, or E to exit:\n").upper()
        if response == 'D':
            demo()
        elif response == 'S':
            shuffle()
        elif response == 'E':
            break
        else:
            print(evalHand(response))


main()
