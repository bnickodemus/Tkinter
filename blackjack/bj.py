try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too

import random
from random import shuffle

SUIT = ['C','D','S','H']
TYPE = ['A','2','3','4','5','6','7','8','9','J','Q','K']
VALUE = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}

class Card():

    def __init__(self,type=None,suit=None):
        if (type or suit) is None:
            self.type = 'X'
            self.suit = 'X'
        else:
            self.type = type
            self.suit = suit
    def __str__(self):
        return "{0.type} of {0.suit}".format(self)
    def getSuit(self):
        return self.suit
    def getType(self):
        return self.type

class Deck():

    def __init__(self):
        self.deck = []
        for i in range(0,4):
            for j in range(0,12):
                c = Card(TYPE[j],SUIT[i])
                self.deck.append(c)
    def __str__(self):
        s = ''
        for c in self.deck:
            s = s + str(c) + '\n'
        return s
    def shuffle(self):
        random.shuffle(self.deck)
    def pop(self):
        return self.deck.pop(0)

class Player():

    def __init__(self):
        self.hand = []
        self.total = 0
    def __str__(self):
        s = ''
        for card in self.hand:
            s = s + str(card) + '\n'
        return s
    def add_card(self, card):
        self.hand.append(card)
    def getValue(self):
        self.total = 0
        for card in self.hand:
            type = card.getType()
            self.total += VALUE[type]
        return self.total
    
    def turn(self, deck):
        end = False
        while (end == False):
            if self.total < 22:
                choice = input("[H]it [S]tand ").lower()
                while choice not in ['H','h','S','s']:
                    print("invalid input")
                    choice = input("would you like to hit or stand > ")
                if choice == 'h':
                    self.hand.append(deck.pop())
                    print("you were dealt a card")
                    print(self, end='')
                    print("total:" + str(self.getValue()) + '\n')
                if choice == 's':
                    print("you stood your total is:" + str(self.getValue()))
                    end = True
            elif self.total == 21:
                print("blackjack")
                break


class Dealer():

    def __init__(self):
        self.hand = []
    def __str__(self):
        s = ''
        for card in self.hand:
            s = s + str(card) + '\n'
        return s
    def add_card(self, card):
        self.hand.append(card)
    def getValue(self):
        self.total = 0
        for card in self.hand:
            type = card.getType()
            self.total += VALUE[type]
        return self.total
    def play(self, deck):
        while self.getValue() < 17:
            dealer.add_card(deck.pop())
        if self.getValue() == 21:
            print("dealer has blackjack")
        if self.getValue() > 21:
            print("dealer has bust")

def init():
    global d, p1, dealer
    print('\n' + "Welcome to blackjack")
    d = Deck()
    d.shuffle()
    p1 = Player()
    dealer = Dealer()
    p1.add_card(d.pop())
    p1.add_card(d.pop())
    print("cards in your hand:" + "\n" + str(p1) + "total:" + str(p1.getValue()) + '\n')
    dealer.add_card(d.pop())
    dealer.add_card(d.pop())
    print("dealers hand:" + '\n' + str(dealer.hand[0]) + '\n' + "*")

def game():
    init() 
    p1.turn(d) 
    dealer.play(d)
    print("dealers hand:")
    print(dealer, end='') 
    print("dealers total:" + str(dealer.getValue()))
    if p1.getValue() < 22:
        if dealer.getValue() > 21:
            print("you win")
        elif p1.getValue() > dealer.getValue():
            print("you win")    
        elif p1.getValue() == dealer.getValue():
                print("push (it's a tie)")

game()




