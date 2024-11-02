import random

class newCard:
    def __init__(self):
        self.value = random.randint(1, 11)
        self.symbol = self.randSymbol()

    def randSymbol(self):
        random.seed()
        symbol = random.randint(1,4)
        match symbol:
            case 1:
                symbol = "Spades"
            case 2:
                symbol = "Ace"
            case 3:
                symbol = "Hearts"
            case 4:
                symbol = "Clubs"
        return symbol
