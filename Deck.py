from Card import card
from random import shuffle

def deck_key():
    deck_card = dict()
    deck_keys = list()
    deck_card = card()
    deck_keys = list(deck_card.keys())
    shuffle(deck_keys)
    return deck_keys

def deck_share(x):
    return x.pop()
