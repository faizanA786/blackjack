import new_card as nc
import new_trump as nt
import game_utils as u
import player as p
import dealer as d
import time

def init():
    playerTDeck = []
    enemyTDeck = []
    playerDeck = [nc.newCard(), nc.newCard()]
    enemyDeck = [nc.newCard(), nc.newCard()]
    u.updateLimit(21)
    p.viewCard(0, playerDeck, playerTDeck, enemyDeck)
    p.viewCard(1, playerDeck, playerTDeck, enemyDeck)
    nextTurn(playerDeck, enemyDeck, playerTDeck, enemyTDeck)

def nextTurn(playerDeck, enemyDeck, playerTDeck, enemyTDeck):
    gameOver = False
    while gameOver == False:
        playerPassed = p.navigate(playerDeck, enemyDeck, playerTDeck)
        dealerPassed = d.determineDecision(playerDeck, enemyDeck)
        if playerPassed and dealerPassed:
            compareScore(playerDeck, enemyDeck)
            gameOver = True
        else:
            print("\nYou have recieved a new trump card!")
            playerTDeck.append(nt.newTrumpCard())
            enemyTDeck.append(nt.newTrumpCard())

def compareScore(playerDeck, enemyDeck):
    playerSum = u.getTotal(playerDeck)
    enemySum = u.getTotal(enemyDeck)

    print("\nYour total " + str(playerSum))
    print("Dealer total " + str(enemySum))

    if playerSum > u.updateLimit(None) and enemySum > u.updateLimit(None):
        print("Game over, nobody wins.")
    elif (playerSum > enemySum or enemySum > u.updateLimit(None)) and playerSum <= u.updateLimit(None):
        print("You win!")
    else:
        print("Game over, you lost to the dealer.")