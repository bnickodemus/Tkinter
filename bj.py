import random

SUIT = ['C','D','S','H']
TYPE = ['A','2','3','4','5','6','7','8','9','J','Q','K']
VALUE = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}

class Card():

    def __init__(self,type,suit):
        self.type = type
        self.suit = suit
    def __str__(self):
        return "{0.type} of {0.suit}".format(self)
    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.value

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
        random.shuffle(self.cards)

# card test
#c = Card("A","S")
#print (c)

#test deck
d = Deck()
print (d)







