import time
import random
import new_card as nc
import game_utils as u

def determineDecision(playerDeck, enemyDeck):
    risk = riskCheck(u.getTotal(enemyDeck), u.getTotal(playerDeck))
    if risk:
        drawCard(enemyDeck)
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

def riskCheck(enemySum, playerSum):
    if enemySum >= u.updateLimit(None) or playerSum > u.updateLimit(None):
        return False
    elif enemySum < u.updateLimit(None):
        random.seed()
        stake = 10 + -(enemySum/u.updateLimit(None))
        probability = (playerSum - enemySum) / stake
        decision = rollDice(probability)
        return decision
    
def rollDice(probability):
    random.seed()
    if random.random() < probability:
        return True
    else:
        return False

def hasTrumpCard():
    pass