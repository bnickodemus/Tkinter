from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image

import random
from random import shuffle

SUIT = ['C','D','S','H']
TYPE = ['A','2','3','4','5','6','7','8','9','J','Q','K']
VALUE = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}
IMAGE = ['ac.gif','2c.gif','3c.gif','4c.gif','5c.gif','6c.gif','7c.gif','8c.gif','9c.gif','10c.gif','jc.gif','qc.gif','kc.gif']

class Card():

    def __init__(self,type=None,suit=None,image=None):
        if (type or suit) is None:
            self.type = 'X'
            self.suit = 'X'
            self.image = "ac.gif"
        else:
            self.type = type
            self.suit = suit
            self.image = image
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
                c = Card(TYPE[j],SUIT[i],IMAGE[j])
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
            if self.total < 21:
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
            else:
                print("bust")
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
    
    print(p1.hand[0].image)
    print('\n'+'\n')
    x=40
    gif1 = PhotoImage(file = p1.hand[0].image)
    canvas.create_image(x, 200, image = gif1, anchor = NW)
    x+=40
    gif2 = PhotoImage(file = p1.hand[1].image)
    canvas.create_image(x, 200, image = gif1, anchor = NW)
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
    if p1.getValue() > dealer.getValue():
        print("you win")
    if dealer.getValue() > 21:
        print("you win")
    elif p1.getValue() == dealer.getValue():
        print("push")
    else:
        print("you lose")

class App:
    master = Tk()

    content = Canvas(master)
    canvas = Canvas(content, borderwidth=5, height=400, width=600, background="Dark Green")
    canvas.pack(expand = YES, fill = BOTH)
    #frame.pack_propagate(0) # don't shrink

    def hitCallback():
        print ("hit!")
    def standCallback():
        print ("stand!")
    
    def printCard(self, card):
        x=400
        img = PhotoImage(file = card.image)
        canvas.create_image(x, 200, image = img, anchor = NW)
    
    hit = Button(content, text="hit", command=hitCallback)
    stand = Button(content, text="stand", command=standCallback)
    content.grid(column=0, row=0)
    canvas.grid(column=0, row=0, columnspan=6, rowspan=6)
    hit.grid(column=0, row=5)
    stand.grid(column=1, row=5)

    x = 100
    gif3 = PhotoImage(file = 'jc.gif')
    canvas.create_image(x, 200, image = gif3, anchor = NW)

    master.mainloop()


game()




