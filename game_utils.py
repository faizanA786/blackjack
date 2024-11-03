def getTotal(deck):
    sum = 0 
    for i in range(len(deck)):
        sum += deck[i].value
    return sum

def updateLimit(newLimit, limit=[0]):
    if newLimit is None:
         return limit[0]
    else:
        limit[0] = newLimit
        return limit[0]
    
def getTrump(trumpVal, playerTDeck):
    match trumpVal:
        case 0:
            for i in range(len(playerTDeck)):
                if trumpVal == playerTDeck[i].trumpVal:
                    playerTDeck.pop(i)
                    return True
        case _:
            return False
                
def useTrump(trumpVal):
    match trumpVal:
        case 0:
            trump27()

def trump27():
    updateLimit(27)

   