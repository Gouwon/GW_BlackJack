from Person import *
from Deck import *

class Player(Person):
    def __init__(self):
        super().__init__()
        self.name = "Player"
        
    
    def decision(self, x):
            isStay = True
            while isStay:
                user_input = input("Hit or Stay??? \n'h' for Hit, 's' for Stay >>> ")
                if user_input == 'h':
                    self.hand.append(deck_share(x))
                    print("{}'s hand = {}".format(self.name, self.hand))
                    self.over_21() ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                    isStay = True
                    return 
                    
                elif user_input == 's':
                    isStay = False
                    return
                else:
                    print("Please make sure your insert key!!")
                    return
    
    def score(self):
        a = super().score()
        print("..............{}'s score = {:d}".format(self.name, a))
        return a