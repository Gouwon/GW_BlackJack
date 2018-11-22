from random import shuffle


# def open_game():
#     print("Welcome to BlackJack Game World!!!")
#     user_input = input("Wanna Gambling? \nPress 's' to Start / 'e' to Exit >>> ")
#     if user_input == 's':
#         game()
#     elif user_input == 'e':
#         print("THANK YOU!! GOOD BYE!!~~")
#         exit()
#     else:
#         print("Wrong Insert. Please give me proper command.")
#         exit()


def card():
    pattern = ['S', 'C', 'H', 'D']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    point = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11'] * 4

    card_form = list()
    card_set = dict()
    for i, j in enumerate(pattern):
        for v, w in enumerate(numbers):
            card_form.append(j + w)
    
    for x in range(52):
        card_set[card_form[x]] = point[x]
    return card_set

def deck_key():
    deck_card = dict()
    deck_keys = list()
    deck_card = card()
    deck_keys = list(deck_card.keys())
    shuffle(deck_keys)
    return deck_keys

def deck_share(x):
    return x.pop()

# def game():
   
#     while True:
#         cards = card()   
#         deck = deck_key()   
#         player = Player()
#         dealer = Dealer()
#         give_2cards(player.hand, dealer.hand, deck)
#         print("Player's hand = ", player.hand)


#         if player.over_21() == False or dealer.over_21() == False:
#             pass
#         else:
#             pf = True
#             df = True
#             while True:
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#                 if player.decision(deck) == False:
#                     break
#                 player.over_21() ## 리턴 while 변수

#             while True:
#                 if dealer.decision(deck) == False:
#                     break
#                 dealer.over_21()
#         outcome(player.score(), dealer.score())  ##3 플레이어와 딜러의 패와 점수들을 인자값 받지 않고 보여줄 방법은?
#         print("88888888888888888888888888")
#         close_game(dealer.score())  ##2 close 내에서 재입력 받는 방법은?
#         print("0000000000")
#         ##1 플레이어 버스트시 딜러의 패와 점수는 어떻게 보여주는가?
#         ##1 딜러 버스트시 플레이어의 패와 점수는 어떻게 보여주는가?
        
        

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
    print("..............Dealer's score =", y)
    
    if x < 21 and y < 21:
        if x == y:
            print("Draw!!!")
        elif x > y:
            print("Player win the game!")   
        else:
            print("Player lost the game!")
    elif x == 21:
        print("Player win the game!")
    elif y == 21:
        print("Player lost the game!")
    elif x < 21 and y > 21:
        print("Player win the game!")
    elif x > 21 and y < 21:
        print("Player lost the game!")
    else:
        pass


def close_game(y):

   
    user_input = input("Wanna continue the game??\nPress 'r' to resume the game or 'q' to quit >>> ")
    if user_input == 'r':    
        return True

    elif user_input == 'q':
        print("THANK YOU FOR YOUR PLAYING!!!")
        exit()

    else:
        print("Please check your Key!") ##2  키 재입력 받는 방법??
        return close_game(y)
    

# def show_record():    ##3 플레이어와 딜러의 패와 점수들을 인자값 받지 않고 보여줄 방법은?