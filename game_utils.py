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
    if len(deck) < 4:
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
                
def useTrump(trumpVal):
    match trumpVal:
        case 0:
            trump27()
        case 1:
            trump17()
        case 2:
            return trumpRefresh()

def trump27():
    time.sleep(1)
    print("The card limit has increased to 27!")
    time.sleep(1)
    updateLimit(27)

def trump17():
    time.sleep(1)
    print("The card limit has decreased to 17!")
    time.sleep(1)
    updateLimit(17)

def trumpRefresh():
    newDeck = [nc.newCard(), nc.newCard()]
    time.sleep(1)
    print("Hand discarded, two new random cards drawn.")
    time.sleep(1)
    return newDeck


   