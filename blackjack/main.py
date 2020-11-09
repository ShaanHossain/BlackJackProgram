import math
import random
import unicodedata
import time
import printcards as PC

def aces(cardlist):
    for c in cardlist:
        if (c.n == 11):
            return True
    return False

def lowerace(cardlist):
    for c in cardlist:
        if (c.n == 11):
            Card.changevalue(c, 1)
            # print("lowered ace")
            break

def comphelper(self):
    self.v = 0
    for c in self.cl:
        self.v = self.v + c.n

    return self.v

class Card:

    def __init__(self, suit, number, type):
        self.s = suit
        self.n = number
        self.t = type

    def changevalue(self, val):
        self.n = val

class Hand:

    def compvalue(self):
        self.v = comphelper(self)

        if(self.v > 21):
            if(aces(self.cl)):
                while(self.v > 21 and aces(self.cl)):
                    lowerace(self.cl)
                    self.v = comphelper(self)
                if(self.v > 21):
                    self.v = 0
            else:
                self.v = 0

        return self.v

    def addcard(self, c):
        self.cl.append(c)

    def __init__(self, cardlist, bet):

        value = 0
        self.b = bet
        self.v = value
        self.cl = cardlist

# x1 = Hand([Card("Spades", 2, "Number"), Card("Clubs", 5, "Number")])
# print(x1.v)

# c1 = Card("Spades", 11, "Ace")
# c2 = Card("Hearts", 5, "Number")

# Hand.addcard(x1, c1)
# print(x1.v)
# Hand.addcard(x1, c2)
# print(x1.v)

# Spade, Club, Diamond, Heart

# test

# deck = []
#
# deck.append(Card("s",1))
#
# print(deck[0].n)

# for i in range (0,13):
#     print(i)

def gendeck():

    deck = []
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    for s in suits:
        for i in range (2,11):
            deck.append(Card(s,i,"Number"))
        deck.append(Card(s, 10,"Jack"))
        deck.append(Card(s, 10,"Queen"))
        deck.append(Card(s, 10,"King"))
        deck.append(Card(s, 11,"Ace"))

    return deck

def printdeck(deck):
    for x in deck:
        if (x.t == "Number"):
            print(str(x.n) + " of " + x.s)
        else:
            print(x.t + " of " + x.s)

def casinodeck():
    bigdeck = []
    for i in range(0,8):
        bigdeck = bigdeck + gendeck()

    random.shuffle(bigdeck)
    return bigdeck

def takecard(deck):
    card = deck[0]
    deck.pop(0)
    return card

def makedealer(deck):
    hand = Hand([takecard(deck)], 0)
    hand.v = Hand.compvalue(hand)
    return hand

def makehand(deck, bet):
    hand = Hand([takecard(deck), takecard(deck)], bet)
    hand.v = Hand.compvalue(hand)
    return hand

def printcards():

    print("Dealer:")
    PC.printhand(dealer)
    print("Player:")
    for i in player:
        PC.printhand(i)

def acedeck():

    deck = []
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    for i in range (0, 4):
        for s in suits:
            deck.append(Card(s, 11,"Ace"))

    return deck

def blackjack(hand):
    return (len(hand.cl) == 2 and Hand.compvalue(hand) == 21)


# printdeck(casinodeck())

# test game

print("Welcome to Blackjack Sim 1.0")
# print("Enter Human Players")
# human = int(input())
# print("Enter AI Players")
# ai = int(input())

# cash = input("Enter starting amount\n")

playing = True
money = 1000.0

while(playing == True):

    turn = True

    deck = casinodeck()

    print("You have " + str(money) + " dollars")
    print("Enter bet value or 0 to exit")
    bet = int(input())
    if (bet == 0):
        break

    dealer = makedealer(deck)
    player = [makehand(deck, bet)]
    money = money - bet

    while(turn == True):

        for i in player:

            printcards()

            if(blackjack(i)):
                money = money + (bet * 2.5)
                player.remove(i)
                print("Blackjack!")
                continue

            print("s to stand, h to hit, d to double, p to split, r to surrender, e to exit")
            choice = input()

            if (choice == "h" or choice == "d"):
                Hand.addcard(i, takecard(deck))
                i.v = Hand.compvalue(i)
                if(choice == "d"):
                    i.b = i.b * 2
                    money = money - bet

            if(choice == "p"):
                player.append(Hand([i.cl[0]], bet))
                player.append(Hand([i.cl[1]], bet))
                player.remove(i)
                money = money - bet

            if(choice == "r"):
                i.v = 0
                money = money + (bet / 2)

            if (i.v == 0 or choice == "s" or choice == "d" or choice == "r" or choice == "e"):
                turn = False
                if (choice == "e"):
                    playing = False
    print()
    printcards()

    while(dealer.v < 17 and dealer.v != 0):
        Hand.addcard(dealer, takecard(deck))
        dealer.v = Hand.compvalue(dealer)
        # print(dealer.v)
        time.sleep(.75)
        printcards()

    for i in player:

        if (dealer.v > i.v or i.v == 0):
            print("You Lose")
            print("Dealer: " + str(dealer.v))
            print("Player: " + str(i.v))
        elif (dealer.v < i.v):
            print("You Win!")
            print("Dealer: " + str(dealer.v))
            print("Player: " + str(i.v))
            money = money + (i.b * 2)
        else:
            print("Push")
            print("Dealer: " + str(dealer.v))
            print("Player: " + str(i.v))
            money = money + bet

# PC.printcard(c1)
# PC.printhand(x1)
