"""
dealer.py

Basic dealer functionality.
Includes methods that let the dealer determine their decision, draw a card (if they deem its safe to) and use logic to decide hen to draw a trump
"""

# dependencies
import time
import random
import new_card as nc
import game_utils as u
import new_trump as nt
from gui import game_page

def determineDecision(pile, playerDeck, enemyDeck, enemyTDeck): # dealer determines what choice to make
    # specialTrump = decideTrump(pile, u.getTotal(playerDeck), u.getTotal(enemyDeck), enemyTDeck, enemyDeck)
    specialTrump = False
    risk = riskCheck(u.getTotal(enemyDeck), u.getTotal(playerDeck))
    if risk and not specialTrump:
        game_page.updateDealerAction(0)
        drawCard(pile, enemyDeck)
        return False
    else:
        print("\nDealer stands...")
        game_page.updateDealerAction(1)
        if not specialTrump:
            return True
        else:
            return False
    #END determineDecision

def drawCard(pile, enemyDeck): # draws a random card for the dealer
    print("\nDealer draws...")
    newCard = pile.pop()
    print("Dealer was dealt a " + str(newCard.value) + " " + newCard.symbol)
    enemyDeck.append(newCard)
    return
    #END drawCard

def decideTrump(pile, playerSum, enemySum, enemyTDeck, enemyDeck): # basic logic for when to use specific trump cards
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
            print("\nDealer used " + str(trumpClass.getName(trumpVal)))
            newDeck = u.useTrump(trumpVal, pile, enemyDeck)
            if newDeck is not None:
                enemyDeck = newDeck
            if trumpVal == 0 or trumpVal == 1:
                specialTrump = True
    return specialTrump
    #END decideTrump


def riskCheck(enemySum, playerSum): # decides whether it is worth drawing a card or not
    if enemySum >= u.updateLimit() or playerSum > u.updateLimit():
        return False
    elif enemySum < u.updateLimit():
        STAKE = 10 + -(enemySum/u.updateLimit())
        probability = (playerSum - enemySum) / STAKE
        return rollDice(probability)
    #END riskCheck
    
def rollDice(probability): # if random number generated is less than probability, then draw card
    random.seed()
    if random.random() <= probability:
        return True
    else:
        return False
    #END rollDice