import time
import random
import new_card as nc
import game_utils as u

def determineDecision(playerDeck, enemyDeck, enemyTDeck):
    risk = riskCheck(u.getTotal(enemyDeck), u.getTotal(playerDeck))
    usedTrump = decideTrump(u.getTotal(playerDeck), u.getTotal(enemyDeck), enemyTDeck)
    if risk:
        drawCard(enemyDeck)
        return False
    elif usedTrump:
        time.sleep(1)
        print("\nDealer stands...")
        time.sleep(1)
        return False
    else:
        time.sleep(1)
        print("\nDealer stands...")
        time.sleep(1)
        return True

def drawCard(enemyDeck):
    time.sleep(1)
    print("\nDealer draws...")
    newCard = nc.newCard()
    time.sleep(1)
    print("Dealer was dealt a " + str(newCard.value) + " " + newCard.symbol)
    enemyDeck.append(newCard)
    time.sleep(1)
    return

def decideTrump(playerSum, enemySum, enemyTDeck):
    decidingTrump = True
    usedTrump = False
    while decidingTrump:
        if u.updateLimit() != 27 and (u.getTrump(0, enemyTDeck) and enemySum <= 27) and (enemySum > u.updateLimit()): # 27
            time.sleep(1)
            print("\nDealer used 27!")
            u.useTrump(0)
            usedTrump = True
        elif u.updateLimit() != 17 and ((u.getTrump(1,enemyTDeck) and enemySum <= 17) and playerSum > 17): # 17
            time.sleep(1)
            print("\nDealer used 17!")
            u.useTrump(1)
            usedTrump = True
        elif u.getTrump(2, enemyTDeck) and enemySum >= u.updateLimit(): # Refresh
            time.sleep(1)
            print("\nDealer used Refresh!")
            u.useTrump(2)
        else:
            decidingTrump = False
    return usedTrump


def riskCheck(enemySum, playerSum):
    if enemySum >= u.updateLimit() or playerSum > u.updateLimit():
        return False
    elif enemySum < u.updateLimit():
        STAKE = 10 + -(enemySum/u.updateLimit())
        probability = (playerSum - enemySum) / STAKE
        decision = rollDice(probability)
        return decision
    
def rollDice(probability):
    random.seed()
    if random.random() <= probability:
        return True
    else:
        return False

def hasTrumpCard():
    pass