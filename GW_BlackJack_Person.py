from GW_BlackJack_Card import card
from GW_BlackJack_Gameplay import *

class Person():
        def __init__(self):
                self.name = str()
                self.hand = list()
                self.point = list()
                print("Person입니다!!!")
        
        def score(self):
                self.point = []
                for i, j in enumerate(self.hand):
                        cards = card()  ##4 'A'의 점수를 1 or 11로 어떻게 정하는가?
                        k = cards[self.hand[i]]
                        self.point.append(int(k))
                        # A = ['DA', 'SA', 'HA', 'CA']
                        try: 
                                remove_a = self.hand.remove("A")
                                if sum(remove_a) > 10:
                                        self.point = sum(remove_a) + (len(self.hand) - len(remove_a))
                        except ValueError:
                               pass
                        a = sum(self.point)
                return a
        
        def over_21(self): ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                score = self.score()
                if score > 21:
                        print("{} is busted!!!".format(self.name))
                        self.show_infor()
                        pass
                elif score == 21:
                        print("{} accomplished BlackJack!!!".format(self.name))
                        self.show_infor()
                        pass
        
        def decision(self):
                return 0
        
        def show_infor(self):
                print("{}'s Score = {}, {}'s Hand = {}".format(self.name, self.score, self.name, self.hand))
        
