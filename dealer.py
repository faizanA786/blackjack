import time
import random
import new_card as nc
import game_utils as u
import new_trump as nt

def determineDecision(pile, playerDeck, enemyDeck, enemyTDeck):
    specialTrump = decideTrump(pile, u.getTotal(playerDeck), u.getTotal(enemyDeck), enemyTDeck, enemyDeck)
    risk = riskCheck(u.getTotal(enemyDeck), u.getTotal(playerDeck))
    if risk and not specialTrump:
        drawCard(pile, enemyDeck)
        return False
    else:
        time.sleep(1)
        print("\nDealer stands...")
        time.sleep(1)
        if specialTrump:
            return True
        else:
            return False

def drawCard(pile, enemyDeck):
    time.sleep(1)
    print("\nDealer draws...")
    newCard = pile.pop()
    time.sleep(1)
    print("Dealer was dealt a " + str(newCard.value) + " " + newCard.symbol)
    enemyDeck.append(newCard)
    time.sleep(1)
    return

def decideTrump(pile, playerSum, enemySum, enemyTDeck, enemyDeck):
    trumpClass = nt.newTrumpCard()
    trumpConditions = {
    0: lambda: u.updateLimit() != 27 and (u.getTrump(0, enemyTDeck) and enemySum <= 27) and (enemySum > u.updateLimit()), # 27
    1: lambda: u.updateLimit() != 17 and ((u.getTrump(1,enemyTDeck) and enemySum <= 17) and playerSum > 17), # 17
    2: lambda: u.getTrump(2, enemyTDeck) and enemySum > u.updateLimit() # Refresh
    }

    specialTrump = False
    for trumpVal, useCondition in trumpConditions.items(): # Allows me to loop through the keys and values, where trumpVal = key and trumpCondition is the value
        if useCondition() and not specialTrump:
            usedTrump = True
            time.sleep(1)
            print("\nDealer used " + str(trumpClass.getName(trumpVal)))
            newDeck = u.useTrump(trumpVal, pile, enemyDeck)
            if newDeck is not None:
                enemyDeck = newDeck
            if trumpVal == 0 or trumpVal == 1:
                specialTrump = True
    return specialTrump


def riskCheck(enemySum, playerSum):
    if enemySum >= u.updateLimit() or playerSum > u.updateLimit():
        return False
    elif enemySum < u.updateLimit():
        STAKE = 10 + -(enemySum/u.updateLimit())
        probability = (playerSum - enemySum) / STAKE
        return rollDice(probability)
    
def rollDice(probability):
    random.seed()
    if random.random() <= probability:
        return True
    else:
        return False