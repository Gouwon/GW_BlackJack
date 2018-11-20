from GW_BlackJack_Card import card
from GW_BlackJack_Deck import *
from GW_BlackJack_Player import *
from GW_BlackJack_Dealer import *

def open_game():
    print("Welcome to BlackJack Game World!!!")
    user_input = input("Wanna Gambling? \nPress 's' to Start / 'e' to Exit >>> ")
    if user_input == 's':
        game()
    elif user_input == 'e':
        print("THANK YOU!! GOOD BYE!!~~")
        exit()
    else:
        print("Wrong Insert. Please give me proper commend.")
        exit()

def game():
    
    while True:
        cards = card()   
        deck = deck_key()   
        player = Player()
        dealer = Dealer()
        give_2cards(player.hand, dealer.hand, deck)
        print("Player's hand = ", player.hand)
        if player.over_21() or dealer.over_21():
            continue
        ##1 플레이어 버스트시 딜러의 패와 점수는 어떻게 보여주는가?
        ##1 딜러 버스트시 플레이어의 패와 점수는 어떻게 보여주는가?
        player.decision(deck)
        dealer.decision(deck)    
        outcome(player.score(), dealer.score())  ##3 플레이어와 딜러의 패와 점수들을 인자값 받지 않고 보여줄 방법은?
        close_game()  ##2 close 내에서 재입력 받는 방법은?

def give_2cards(x, y, z):
    for i in range(2):
        x.append(deck_share(z))
        y.append(deck_share(z))
    if y[0] <= y[1]:
        print("Dealer's hand = {}".format(y[0]))
    else:
        print("Dealer's hand = {}".format(y[1]))

def outcome(x, y):
    ##3 플레이어와 딜러의 패와 점수들을 인자값 받지 않고 보여줄 방법은?
    if x == y:
        print("Draw!!!")
    elif x > y:
        print("Player win the game!")   
    else:
        print("Player lost the game!")

def close_game():
    isClose = True
    while isClose:  
        user_input = input("Wanna continue the game??\nPress 'r' to resume the game or 'q' to quit >>> ")
        if user_input == 'r':
            return True
        elif user_input == 'q':
            print("THANK YOU FOR YOUR PLAYING!!!")
            exit()
        else:
            print("Please check your Key!") ##2  키 재입력 받는 방법??
            return not True

# def show_record():    ##3 플레이어와 딜러의 패와 점수들을 인자값 받지 않고 보여줄 방법은?