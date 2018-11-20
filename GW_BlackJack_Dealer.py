from GW_BlackJack_Person import *
from GW_BlackJack_Deck import *
class Dealer(Person):
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
        print("Dealer입니다!!!!!")
    
    def decision(self, x):
        isStay = 0
        while isStay != 0:
            if self.score() < 17:
                self.hand.append(deck_share(x))
                self.over_21()
                isStay = 1
            else:
                break