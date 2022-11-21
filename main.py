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
            self.number = number
        self.suit = input[-1]


def main():
    example_hand = "AS, 10C, 10H, 3D, 3S"
    hand = example_hand.split(", ")
    cards = []
    for card in hand:
        cards.append(Card(card))
    for card in cards:
        print("{} of {}".format(card.number, card.suit))


main()
