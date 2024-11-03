import new_card as nc
import player as p
import dealer as d
import time

def init():
    playerDeck = [nc.newCard(), nc.newCard()]
    enemyDeck = [nc.newCard(), nc.newCard()]
    p.viewCard(0, playerDeck, enemyDeck)
    p.viewCard(1, playerDeck, enemyDeck)
    nextTurn(playerDeck, enemyDeck)

def nextTurn(playerDeck, enemyDeck):
    gameOver = False
    while gameOver == False:
        playerPassed = p.navigate(playerDeck, enemyDeck)
        dealerPassed = d.determineDecision(playerDeck, enemyDeck)
        if playerPassed and dealerPassed:
            compareScore(playerDeck, enemyDeck)
            gameOver = True

def compareScore(playerDeck, enemyDeck):
    playerSum = 0
    enemySum = 0
    for i in range(len(playerDeck)):
        playerSum  += playerDeck[i].value
    for i in range(len(enemyDeck)):
        enemySum  += enemyDeck[i].value

    if playerSum > enemySum and playerSum <= 21:
        print("Game over.")
    else:
        print("You win!")

