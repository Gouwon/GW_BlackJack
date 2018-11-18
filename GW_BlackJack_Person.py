from GW_BlackJack_Card import card
class Person():
        def __init__(self):
                self.name = str()
                self.hand = list()
                self.point = list()
                print("Person입니다!!!")
        
        def score(self):
                for i in self.hand:
                        cards = card()
                        self.point.append(cards[self.hand[i]])
                return self.point
        
        def bust(self): ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                if self.score > 21:
                        print("{}'s score = {:d}".format(self.name, self.score) )
                        print("You are busted!!!")
                        return False
                elif self.score == 21:
                        print("{}'s score = {:d}".format(self.name, self.score) )
                        print("You accomplished the BlackJack!!!")
                        return False
                else:
                        return True
        
        def decision(self):
                return 0
        