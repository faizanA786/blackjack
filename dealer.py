import time
import random
import new_card as nc

def determineDecision(playerDeck, enemyDeck):
    enemySum = 0
    for i in range(len(enemyDeck)):
        enemySum += enemyDeck[i].value
    if enemySum < 21:
        drawCard(enemyDeck)
    else:
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
