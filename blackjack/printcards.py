# basic test card

spade = u'\u2660'
club = u'\u2663'
heart = u'\u2665'
diamond = u'\u2666'

def setcard (card):
    lst = []
    if (card.n == 10 and card.t == "Number"):
        value1 = str(card.n)
        value2= str(card.n)
    elif (card.t != "Number"):
        value1 = " " + card.t[0]
        value2 = card.t[0] + " "
    else:
        value1 = str(" " + str(card.n))
        value2 = str(str(card.n) + " ")

    if(card.s == "Spades"):
        suit = spade
    elif(card.s == "Clubs"):
        suit = club
    elif(card.s == "Hearts"):
        suit = heart
    else:
        suit = diamond

    lst.append("|---------|")
    lst.append("|" + value1 + "       |")
    lst.append("| " + suit + "       |")
    lst.append("|         |")
    lst.append("|       " + suit + " |")
    lst.append("|       " + value2 + "|")
    lst.append("|---------|")

    return lst

def printcard (card):
    lst = setcard(card)
    for i in lst:
        print(i)

def printhand (hand):
    lst = []
    for c in hand.cl:
        lst.append(setcard(c))

    for i in range (0, 7):
        for x in lst:
            print(x[i], end =" ")
        print()
