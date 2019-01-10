import Gameplay


class Person:
    def __init__(self):
        self.name = ''
        self.hand = []
        self.point = []

    def score(self):
        self.point = []

        for i in self.hand:
            cards = Gameplay.card()  # 4 'A'의 점수를 1 or 11로 어떻게 정하는가?
            k = cards[i]
            self.point.append(int(k))
        a = sum(self.point)
        if a > 21 and self.point.count(11) != 0:  # A가 있으면
            a_value = self.point.count(11)
            total_value = sum(self.point)
            a = total_value - (a_value * 10)
            return int(a)
        elif a > 21 and self.point.count(11) == 0:
            return int(a)
        elif a < 21:
            return int(a)   
        else:
            return int(a)     
        
    def over_21(self):  # 1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
        score = self.score()

        if score > 21:
            print("{} is busted!!!".format(self.name))
            return False

        elif score == 21:
            print("{} accomplished BlackJack!!!".format(self.name))
            return False

        else:
            return True

    def decision(self, isStay):
        return 0

    def show_infor(self):
        print("{}'s Score = {}, {}'s Hand = {}".format(
            self.name, self.score(), self.name, self.hand))

######################### Player #######################


class Player(Person):
    def __init__(self):
        super().__init__()
        self.name = "Player"
        print("{}가 입장하였습니다.".format(self.name))

    def decision(self, x):
        user_input = input("Hit or Stay??? \n'h' for Hit, 's' for Stay >>> ")
        if user_input == 'h':
            self.hand.append(Gameplay.deck_share(x))
            print("{}'s hand = {}".format(self.name, self.hand))
            # 1 자식인스턴스의 버스트 시, 모든 자식 인스턴스들의 attribute를 보여줄 방법은?
            return True
        elif user_input == 's':
            return False
        else:
            print("Please make sure your insert key!!")

    def score(self):
        a = super().score()
        print("..............{}'s score = {}".format(self.name, a))
        return a


class Dealer(Person):
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
        print("{}가 입장하였습니다.".format(self.name))

    def decision(self, x):
        
        if self.score() > 17:
            return False
        else:
            self.hand.append(Gameplay.deck_share(x))
            return True
