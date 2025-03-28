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
        return f"{self.rank} - {self.suit}"


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
    score = 0
    current_card = deck.deal()
    print(f"Текщая карта: {current_card}")

    while deck.cards:
        guess = input("Больше или меньше? (+/-):").lower()
        next_card = deck.deal()
        print(f"Следующая карта: {next_card}")

        if guess == "+":
            if next_card.value > current_card.value:
                print("Правильно!")
                score += 1
            else:
                print("Неправильно!")
        elif guess == "-":
            if next_card.value < current_card.value:
                print("Правильно!")
                score += 1
            else:
                print("Неправильно!")
        else:
            print("Неверный ввод")

        current_card = next_card
    print(f"Игра закончена со счетом: {score}")

play()
