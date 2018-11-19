from GW_BlackJack_Person import *
from GW_BlackJack_Deck import *

class Player(Person):
    def __init__(self):
        super().__init__()
        self.name = "Player"
        print("Player입니다!!!!!")
    
    def decision(self, x):
        isStay = 0
        while isStay == 0:
            user_input = input("Hit or Stay??? \n'h' for Hit, 's' for Stay >>> ")
            if user_input == 'h':
                self.hand.append(deck_share(x))
                print("{}'s hand = {}".format(self.name, self.hand))
                self.bust() ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                isStay = 1
            elif user_input == 's':
                break
            else:
                print("Please make sure your insert key!!")
                continue