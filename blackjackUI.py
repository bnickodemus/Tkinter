from tkinter import *
from tkinter import ttk
#from PIL import ImageTk, Image

import random
from random import shuffle

SUIT = ['C','D','S','H']
TYPE = ['A','2','3','4','5','6','7','8','9','J','Q','K']
VALUE = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}
IMAGE = ['ac.gif','2c.gif','3c.gif','4c.gif','5c.gif','6c.gif','7c.gif','8c.gif','9c.gif','jc.gif','qc.gif','kc.gif','ad.gif','2d.gif','3d.gif','4d.gif','5d.gif','6d.gif','7d.gif','8d.gif','9d.gif','jd.gif','qd.gif','kd.gif','as.gif','2s.gif','3s.gif','4s.gif','5s.gif','6s.gif','7s.gif','8s.gif','9s.gif','js.gif','qs.gif','ks.gif','ah.gif','2h.gif','3h.gif','4h.gif','5h.gif','6h.gif','7h.gif','8h.gif','9h.gif','jh.gif','qh.gif','kh.gif']

X = 0 # represents the X coordinate on the canvas for displaying players cards
Z = 0 # represents the X coordinate on the canvas for displaying dealers cards

class Card():

    def __init__(self,type=None,suit=None,image=None):
        if (type or suit or image) is None:
            self.type = 'X'
            self.suit = 'X'
            self.image = 'ac.gif'
        else:
            self.type = type
            self.suit = suit
            self.image = image
    def __str__(self):
        return "{0.type} of {0.suit}  img: {0.image}".format(self)
    def getSuit(self):
        return self.suit
    def getType(self):
        return self.type

class Deck():

    def __init__(self):
        self.deck = []
        counter = 0
        for i in range(0,4):
            for j in range(0,12):
                c = Card(TYPE[j],SUIT[i],IMAGE[counter])
                counter += 1
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
        self.total = 0 #sum of cards
        self.handTotal = 0 #number of cards
    def __str__(self):
        s = ''
        for card in self.hand:
            s = s + str(card) + '\n'
        return s
    def add_card(self, card):
        self.hand.append(card)
        self.handTotal += 1
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
        self.total = 0 #sum of cards
        self.handTotal = 0 #number of cards
    def __str__(self):
        s = ''
        for card in self.hand:
            s = s + str(card) + '\n'
        return s
    def add_card(self, card):
        self.hand.append(card)
        self.handTotal += 1
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

def init(board):
    global deck, p1, dealer, X, Z
    print('\n' + "Welcome to blackjack")
    deck = Deck()

    #print(str(d) +'\n'+'\n')

    deck.shuffle()
    p1 = Player()
    dealer = Dealer()
    
    p1.add_card(deck.pop())
    p1.add_card(deck.pop())
    
    print("cards in your hand:" + "\n" + str(p1) + "total:" + str(p1.getValue()) + '\n')
    
    board.printCard(50,280,p1.hand[0])
    board.printCard(150,280,p1.hand[1])
    
    X += 250
    
    dealer.add_card(deck.pop())
    dealer.add_card(deck.pop())
    
    print("dealers hand:" + '\n' + str(dealer.hand[0]) + '\n' + "*" + '\n')
    board.printCard(50,100,dealer.hand[0])
    
    print("total:" + str(p1.getValue()))
    
    Z += 150


def game(board):
    init(board)
    #p1.turn(d)
    #dealer.play(d)



def hitCallback():
    global X
    #print ("hit!")
    
    p1.hand.append(deck.pop())
    board.printCard(X,280,p1.hand[p1.handTotal])
    X += 100
    p1.handTotal += 1 # .append does not take to account the handTotal
    print ("total:" + str(p1.getValue()))
    if p1.getValue() > 21:
        #print ("you lose")
        board.printImage(190,25,'lose.gif')

def standCallback():
    global deck, Z
    #print ("stand!")
    #call dealer ai
    if p1.getValue() < 22:
        dealer.getValue()
        dealer.play(deck)
        dealer.getValue()
        i = 1 # first card was already printed
        while (i < dealer.handTotal):
            board.printCard(Z,100,dealer.hand[i])
            Z += 100
            i += 1
        if dealer.getValue() > 21:
            print("dealer val > 21:" + str(dealer.getValue()))
            board.printImage(190,25,'win.gif')
        elif p1.getValue() == dealer.getValue():
            board.printImage(150,25,'push.gif')
        elif p1.getValue() > dealer.getValue():
            print("player sum > dealer sum:" + str(p1.getValue()) + " " + str(dealer.getValue()))
            board.printImage(190,25,'win.gif')
        elif p1.getValue() < dealer.getValue():
            board.printImage(190,25,'lose.gif')
    elif p1.getValue() > 21:
        board.printImage(190,25,'lose.gif')





def resetCallback():
    global X,Z
    X = 0 #reset player X cord.
    Z = 0 #reset dealer Z cord.
    board.canvas.delete("all") # reset the canvas
    # reset grid and text
    board.content.grid(column=0, row=0)
    board.canvas.grid(column=0, row=0, columnspan=8, rowspan=8)
    board.canvas.create_text(50,25, anchor=NW,  font=("Helvetica",34), text="                     BlackJack")
    board.canvas.create_text(50,70, anchor=NW,  font=("Helvetica",18), text="Dealers Hand:")
    board.canvas.create_text(50,240, anchor=NW,  font=("Helvetica",18), text="Your Hand:")

    game(board)


class Background:

    def __init__(self,master):
        
        content = Canvas(master)
        self.content = content
        canvas = Canvas(content, borderwidth=5, height=450, width=600, background="Dark Green")
        self.canvas = canvas
        self.canvas.pack(expand = YES, fill = BOTH)
        
        hit = Button(content, text="hit", command=hitCallback)
        stand = Button(content, text="stand", command=standCallback)
        reset = Button(content, text="start/reset", command=resetCallback)
        
        #creates a larger grid to place elements
        content.grid(column=0, row=0)
        canvas.grid(column=0, row=0, columnspan=8, rowspan=8)
        canvas.create_text(50,25, anchor=NW,  font=("Helvetica",34), text="                     BlackJack")
        canvas.create_text(50,70, anchor=NW,  font=("Helvetica",18), text="Dealers Hand:")
        canvas.create_text(50,240, anchor=NW,  font=("Helvetica",18), text="Your Hand:")
    
        hit.grid(column=0, row=7)
        stand.grid(column=1, row=7)
        reset.grid(column=2, row=7)
    
    def printCard(self, x, y, card):
        photo = PhotoImage(file=card.image)
        label = Label(image=photo)
        label.image = photo # keeps a ref so python doesn't gabage collect the image
        self.canvas.create_image(x, y, image=label.image, anchor = NW)

    def printImage(self, x, y, pic):
        photo = PhotoImage(file=pic)
        label = Label(image=photo)
        label.image = photo # keeps a ref so python doesn't gabage collect the image
        self.canvas.create_image(x, y, image=label.image, anchor = NW)

    
root= Tk()
board = Background(root)

#card1 = Card(TYPE[0],SUIT[0],IMAGE[0])
#board.printCard(100,card1)
root.mainloop()





