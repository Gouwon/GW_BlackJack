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
                # if len(self.hand) == 2:
                #         self.hand.pop(0)
                #         self.hand.append('CA') #QQQ
                for i, j in enumerate(self.hand):
                        cards = card()  ##4 'A'의 점수를 1 or 11로 어떻게 정하는가?
                        k = cards[self.hand[i]]
                        self.point.append(int(k))
                        A = ['DA', 'SA', 'HA', 'CA']
                        if sum(self.point) > 21:
                                print("xxxxxxxxxxxxxxxxxxxxxxx")    
                                try: 
                                        hasA = False
                                        for i in self.hand:
                                                for i in A:
                                                        hasA = True
                                                        break
                                                if hasA:
                                                       remove_a = self.hand.remove(i)
                                                       self.point = sum(remove_a) + (len(self.hand) - len(remove_a)) 
                                                        

                                        # # filter(lambda) 
                                        # print("QQQQQ>>", A[0] in self.hand or A[1] in self.hand or A[2] in self.hand or A[3] in self.hand, self.hand)
                                        # for i in A
                                        # if A[0] in self.hand or A[1] in self.hand or A[2] in self.hand or A[3] in self.hand:
                                        #         remove_a = self.hand.remove(A)
                                        #         if sum(remove_a) > 10:
                                        #                 self.point = sum(remove_a) + (len(self.hand) - len(remove_a))

                                except ValueError:
                                        pass
                        a = sum(self.point)
                return a
        
        def over_21(self): ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                score = self.score()
                if score > 21:
                        print("{} is busted!!!".format(self.name))
                        self.show_infor()
                        return True
                elif score == 21:
                        print("{} accomplished BlackJack!!!".format(self.name))
                        self.show_infor()
                        return True

        
        def decision(self):
                return 0
        
        def show_infor(self):
                print("{}'s Score = {}, {}'s Hand = {}".format(self.name, self.score(), self.name, self.hand))
        
