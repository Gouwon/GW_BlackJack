from GW_BlackJack_Card import card
class Person():
        def __init__(self):
                self.name = str()
                self.hand = list()
                self.point = list()
                print("Person입니다!!!")
        
        def score(self):
                print(len(self.hand))
                for i, j in enumerate(self.hand):
                        cards = card()  ##4 'A'의 점수를 1 or 11로 어떻게 정하는가?
                        k = cards[self.hand[i]]
                        self.point.append(int(k))
                        A = ['DA', 'SA', 'HA', 'CA']
                        try: 
                                remove_a = self.hand.remove("A")
                                if sum(remove_a) > 10:
                                        self.point = sum(remove_a) + (len(self.hand) - len(remove_a))
                        except ValueError:
                               pass
                        a = sum(self.point)
                        print("iiiiiiiiiiiiiii", i)
                        print("jjjjjjjjjjjjjj", j)
                        print("score 안입니다.!!!!!", a)
                        print(self.hand)
                return a
        
        def over_21(self): ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                score = self.score()
                if score > 21:
                        print("{}'s score = {:d}".format(self.name, score))
                        print("You are busted!!!")
                        return
                elif score == 21:
                        print("{}'s score = {:d}".format(self.name, score))
                        print("You accomplished BlackJack!!!")
                        return
        
        def decision(self):
                return 0
        
        def show_infor(self):
                print("{}'s Score = {}, {}'s Hand = {}".format(self.name, self.score, self.name, self.hand))
        
