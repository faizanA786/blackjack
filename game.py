import new_card as nc
import new_trump as nt
import game_utils as u
from userstats import updateStats
import player as p
import dealer as d
import time

def init(userID, playerScore=0, dealerScore=0):
    playerTDeck = []
    enemyTDeck = []
    pile = []

    for i in range(312):
        pile.append(nc.newCard())

    playerDeck = [pile.pop(), pile.pop()]
    enemyDeck = [pile.pop(), pile.pop()]

    u.updateLimit(21)
    p.viewCard(0, playerDeck, playerTDeck, enemyDeck)
    p.viewCard(1, playerDeck, playerTDeck, enemyDeck)
    nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore)

def nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore):
    roundOver = False
    while roundOver == False:
        playerPassed:bool = p.navigate(pile, playerDeck, enemyDeck, playerTDeck)
        dealerPassed:bool = d.determineDecision(pile, playerDeck, enemyDeck, enemyTDeck)

        if playerPassed and dealerPassed:
            roundOver = True
            compareScore(userID, playerDeck, enemyDeck, playerScore, dealerScore)
        else:
            if u.dupeTrump(playerTDeck) == True:
                print("\nYou have recieved a new trump card!")
            else:
                print("\nYou have not recieved a new trump card, trump card deck full!")
            u.dupeTrump(enemyTDeck)


def compareScore(userID, playerDeck, enemyDeck, playerScore, dealerScore):
    playerSum = u.getTotal(playerDeck)
    enemySum = u.getTotal(enemyDeck)

    print("\nYour total " + str(playerSum))
    print("Dealer total " + str(enemySum))

    if playerSum > u.updateLimit(None) and enemySum > u.updateLimit(None):
        print("Round over, nobody wins.")
    elif (playerSum > enemySum or enemySum > u.updateLimit(None)) and playerSum <= u.updateLimit(None):
        print("Round over, the dealer has lost!")
        playerScore += 1
        print("Player : " + str(playerScore) + "/3")
        print("Dealer : " + str(dealerScore) + "/3")
        if playerScore == 3:
            print("\nYou are the winner!")
            updateStats(userID, 0)
        else:
            time.sleep(1)
            print("\nStarting next round...")
            time.sleep(1)
            init(userID, playerScore, dealerScore)
    else:
        print("Round over, you lost to the dealer.")
        dealerScore += 1
        print("Player : " + str(playerScore) + "/3")
        print("Dealer : " + str(dealerScore) + "/3")
        if dealerScore == 3:
            print("\nGame over.")
            updateStats(userID, 1)
        else:
            time.sleep(1)
            print("\nStarting next round...")
            time.sleep(1)
            init(userID, playerScore, dealerScore)