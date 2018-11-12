## 이 곳은 다른 Class에서 선언된 객체들을 호출하여 게임을 진행하는 곳입니다.



## ================== ##

""" import random

print("Welcome to BlackJack World!!! \n")
user_input = input("Press 's' button to play the game!! \n(Exit Game 'e') >> ")
if user_input == 's':
    card = ["카드"]
    deck = card.shuffle()
    dealer_hand = deck[0], deck[2]
    player_hand = deck[1], deck[3]

    if dealer_hand => 21 or player_hand >=21:
        print("The game is now over!")
        exit()

    elif dealer_hand < 21 or player_hand < 21:
        if dealer_hand <= 16:
            dealer_hand = dealer_hand.append()
        elif dealer_hand => 17:
            return dealer_hand
        
        print("Hit or Stay?")
        user_decision_input = input("'h' for Hit / 's' for Stay")
        if user_decision_input == "h":
            player_hand = player_hand.append()
        elif user_decision_input == "s":
            return player_hand

            
    


elif user_input == 'e':
    print("Thank you for Playing!!!") 
    exit() """