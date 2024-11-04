import new_card as nc
import new_trump as nt
import game_utils as u
import player as p
import dealer as d
import time

def init(playerScore=0, dealerScore=0):
    playerTDeck = []
    enemyTDeck = []
    playerDeck = [nc.newCard(), nc.newCard()]
    enemyDeck = [nc.newCard(), nc.newCard()]
    u.updateLimit(21)
    p.viewCard(0, playerDeck, playerTDeck, enemyDeck)
    p.viewCard(1, playerDeck, playerTDeck, enemyDeck)
    nextRound(playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore)

def nextRound(playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore):
    roundOver = False
    while roundOver == False:
        playerPassed:bool = p.navigate(playerDeck, enemyDeck, playerTDeck)
        dealerPassed:bool = d.determineDecision(playerDeck, enemyDeck, enemyTDeck)
        if playerPassed and dealerPassed:
            roundOver = True
            compareScore(playerDeck, enemyDeck, playerScore, dealerScore)
        else:
            print("\nYou have recieved a new trump card!")
            playerTDeck.append(nt.newTrumpCard())
            enemyTDeck.append(nt.newTrumpCard())

def compareScore(playerDeck, enemyDeck, playerScore, dealerScore):
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
        else:
            time.sleep(1)
            print("\nStarting next round...")
            time.sleep(1)
            init(playerScore, dealerScore)
    else:
        print("Round over, you lost to the dealer.")
        dealerScore += 1
        print("Player : " + str(playerScore) + "/3")
        print("Dealer : " + str(dealerScore) + "/3")
        if dealerScore == 3:
            print("\nGame over.")
        else:
            time.sleep(1)
            print("\nStarting next round...")
            time.sleep(1)
            init(playerScore, dealerScore)