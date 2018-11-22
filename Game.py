import Gameplay 
import Person

print("Welcome to BlackJack Game World!!!")
user_input = input("Wanna Gambling? \nPress 's' to Start / 'e' to Exit >>> ")
if user_input == 's':
    while True:
        cards = Gameplay.card()   
        deck = Gameplay.deck_key()   
        player = Person.Player()
        dealer = Person.Dealer()
        Gameplay.give_2cards(player.hand, dealer.hand, deck)
        print("Player's hand = ", player.hand)


        if player.over_21() == False or dealer.over_21() == False:
            pass
        else:
            while True:
                
                if player.decision(deck) == False:
                    break
                if player.over_21() == False: ## 리턴 while 변수
                    break
            while True:
                if dealer.decision(deck) == False:
                    break
                if dealer.over_21() == False:
                    break
        Gameplay.outcome(player.score(), dealer.score())  ##3 플레이어와 딜러의 패와 점수들을 인자값 받지 않고 보여줄 방법은?
        Gameplay.close_game(dealer.score())  ##2 close 내에서 재입력 받는 방법은?
elif user_input == 'e':
    print("THANK YOU!! GOOD BYE!!~~")
    exit()
else:
    print("Wrong Insert. Please give me proper command.")
    exit()

