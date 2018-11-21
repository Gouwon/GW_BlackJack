from Person import *
from Deck import *
class Dealer(Person):
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
        
    
    def decision(self, x):
        isStay = 1
        print("#################################")
        while isStay != 0:
            if self.score() < 17:
                self.hand.append(deck_share(x))
                self.over_21()

                isStay = 1
            else:
                break