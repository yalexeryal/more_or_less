import random
suits = ('Пики', 'Червы', 'Трефы', 'Бубны')
ranks = ('T', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()


    def _get_value(self):
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == "T":
            return 10
        elif self.rank in ("J", "Q", "K"):
            return 11
        elif self.rank == "A":
            return 14
        else:
            return 0

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Cards(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        return self.cards.pop()


def play():
    deck = Deck()
    player1 = []
    player2 = []

    for _ in range(len(deck.cards) // 2):
        player1.append(deck.deal())
        player2.append(deck.deal())

    while len(player1) and len(player2):
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        print(f"Игрок 1: {card1}, Игрок 2: {card2}")

        if card1.value > card2.value:
            player1.extend([card1, card2])
            print("Игрок 1 выигрывает раунд!")
        elif card1.value < card2.value:
            player2.extend([card2, card1])
            print("Игрок 2 выигрывает раунд!")

        else:
            print("Ничья!")

    if player1:
        print("Игрок 1 выигрывает игру!")
    else:
        print("Игрок 2 выигрывает игру!")


play()
