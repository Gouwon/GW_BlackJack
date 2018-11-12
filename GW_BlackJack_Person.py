""" class Person:
    name = "person"

    def __init__(self):
        self.name """
    
    

## self.name
## Person의 카드의 합 ====> 딜러 / 플레이어의 카드의 합
### def sum(self)
###     카드 class에서 카드를 받아서 그 합을 구하는 부분.
###     card.value

## Hit / Stay 할지의 판단을 하는 부분
### def ask(self)
###     if self.sum > 21 or self.sum = 21:
###         break
###     else:
###         진행     

## Hit / Stay 함수 부분.
### def hit(self):
### def stay(self):

### Hit/ Stay인지 bool형으로 물어봐야지, 그 값들만 비교해서 루프를 돌릴 수 있다.