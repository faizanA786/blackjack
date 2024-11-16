import time
import new_card as nc
import new_trump as nt

def getTotal(deck):
    sum = 0 
    for i in range(len(deck)):
        sum += deck[i].value
    return sum

def updateLimit(newLimit=None, limit=[21]):
    if newLimit is None:
         return limit[0]
    else:
        limit[0] = newLimit
        return limit[0]
    
def dupeTrump(deck):
    if len(deck) < 3:
        genNewTrump = False
        while not genNewTrump:
            newTrump = nt.newTrumpCard()
            if not any(newTrump.trumpVal == card.trumpVal for card in deck):
                deck.append(newTrump)
                return True
                
def getTrump(trumpVal, Tdeck):
    for i in range(len(Tdeck)):
        if trumpVal == Tdeck[i].trumpVal:
            Tdeck.pop(i)
            return True
    return False
                
def useTrump(trumpVal, pile=None, deck=None):
    match trumpVal:
        case 0:
            trump27()
        case 1:
            trump17()
        case 2:
            return trumpRefresh(pile)
        case 3:
            trumpDiscard(pile, deck)

def trump27():
    updateLimit(27)
    time.sleep(1)
    print("The card limit has increased to 27!")
    time.sleep(1)

def trump17():
    updateLimit(17)
    time.sleep(1)
    print("The card limit has decreased to 17!")
    time.sleep(1)

def trumpRefresh(pile):
    newDeck = [pile.pop(), pile.pop()]
    time.sleep(1)
    print("Hand discarded, two cards from pile drawn.")
    time.sleep(1)
    return newDeck

def trumpDiscard(pile, deck):
    last = len(deck)-1
    card = deck.pop()
    pile.append(card)
    time.sleep(1)
    print("Last card discarded.")
    time.sleep(1)

   