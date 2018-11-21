from Card import card
import Gameplay


class Person():
        def __init__(self):
                self.name = str()
                self.hand = list()
                self.point = list()
                
        
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

                        if sum(self.point) > 21 and self.point.count(11) != 0: #A가 있으면 
                                
                                # try: 
                                a_value = self.point.count(11)
                                total_value = sum(self.point)

                                a = total_value - (a_value * 10)
                                return a

                        a = sum(self.point)
                return a
                                # except ValueError:
                                        # pass
                                        # hasA = False
                                        # for i in self.hand:
                                        #         for i in A:
                                        #                 hasA = True
                                        #                 break
                                        #         if hasA:
                                        #                 if self.point == 11:

                                        #                 remove_a= list()
                                        #                 self.point = sum(remove_a) + (len(self.hand) - len(remove_a)) 
                                                        
        
        def over_21(self): ##1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
                score = self.score()
                if score > 21:
                        print("{} is busted!!!".format(self.name))
                        Gameplay.close_game(self.score())
                            
                elif score == 21:
                        print("{} accomplished BlackJack!!!".format(self.name))
                        Gameplay.close_game(self.score())

                else:
                        return True
        
        def decision(self, isStay):
                return 0
        
        def show_infor(self):
                print("{}'s Score = {}, {}'s Hand = {}".format(self.name, self.score(), self.name, self.hand))
        
        def __del__(self):
                return