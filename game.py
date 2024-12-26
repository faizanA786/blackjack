"""
game.py

The module in which the game actually takes place in.
Initialises a round, and controls the turn based gameplay.
"""

# dependencies
from gui import game_page
import new_card as nc
import new_trump as nt
import game_utils as u
from userstats import updateStats
import player as p
import dealer as d
import time


def init(userID, playerScore, dealerScore, window): # initialises a new round
    playerTDeck = []
    enemyTDeck = []
    pile = []

    for i in range(312):
        pile.append(nc.newCard())

    playerDeck = [pile.pop(), pile.pop()]
    enemyDeck = [pile.pop(), pile.pop()]
    u.updateLimit(21)

    dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit = game_page.initDeck(window, playerDeck, enemyDeck)
    print("init draw stand buttons")
    game_page.updatePlayerButtons(window, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)
    window.after(1000, lambda: nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit))
    print("Round Started")
    #END init

def nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, playerPassed=None): # controls the flow of the turn-based gameplay
    roundCondition = False
    def processRound(roundCondition):
        if roundCondition == False:
            if playerPassed is not None:
                game_page.updateDeck(playerDeck, enemyDeck, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)

                dealerPassed:bool = d.determineDecision(pile, playerDeck, enemyDeck, enemyTDeck)
                game_page.updateDeck(playerDeck, enemyDeck, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)

                if playerPassed and dealerPassed: # if both players stand, end round
                    roundCondition = True
                    compareScore(userID, playerDeck, enemyDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)
                else: # insert a new trump into both decks
                    if u.dupeTrump(playerTDeck) == True:
                        print("\nYou have recieved a new trump card!")
                        game_page.updateDeck(playerDeck, enemyDeck, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)
                    else:
                        print("\nYou have not recieved a new trump card, trump card deck full!")
                    u.dupeTrump(enemyTDeck)
                    print("added draw stand buttons")
                    game_page.updatePlayerButtons(window, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)

    processRound(roundCondition)
    #END nextRound


def compareScore(userID, playerDeck, enemyDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit): # compares the two sum values of decks, and declares the appropriate winner
    playerSum = u.getTotal(playerDeck)
    enemySum = u.getTotal(enemyDeck)

    print("\nYour total " + str(playerSum))
    print("Dealer total " + str(enemySum))

    if playerSum > u.updateLimit(None) and enemySum > u.updateLimit(None):
        print("Round over, nobody wins.")
    elif (playerSum > enemySum or enemySum > u.updateLimit(None)) and playerSum <= u.updateLimit(None):
        print("Round over, the dealer has lost!")
        playerScore += 1
        game_page.updateScores(playerScore, dealerScore)
        print("Player : " + str(playerScore) + "/3")
        print("Dealer : " + str(dealerScore) + "/3")
        if playerScore == 3:
            print("\nYou are the winner!")
            updateStats(userID, 0) # adds +1 to the players win stat
            
        else:
            print("\nStarting next round...")
            game_page.deleteLabels(dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)
            window.after(1000, lambda: init(userID, playerScore, dealerScore, window))
    else:
        print("Round over, you lost to the dealer.")
        dealerScore += 1
        game_page.updateScores(playerScore, dealerScore)
        print("Player : " + str(playerScore) + "/3")
        print("Dealer : " + str(dealerScore) + "/3")
        if dealerScore == 3:
            print("\nGame over.")
            updateStats(userID, 1) # adds a +1 to the players loss stat
        else:
            print("\nStarting next round...")
            game_page.deleteLabels(dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit)
            window.after(1000, lambda: init(userID, playerScore, dealerScore, window))
    #END compareScore
