"""
game_page.py

Methods that deal with all operations linked to actual gameplay
"""

#dependencies
from game import *
from player import *
from tkinter import *
from game_utils import *

def updateScores(playerScore, dealerScore, action=None, state=[None]):
    if state[0] is None:
        state[0] = action
    state[0].config(text="Dealer: " + str(dealerScore) + "/3\n" + "Player: " + str(playerScore) + "/3")

    if playerScore == 3 or dealerScore == 3:
        pass

def updatePlayerAction(action, state=[None]):
    if state[0] is None:
        state[0] = action
    elif action == 0: # draw
        state[0].config(text="You: Draw")
    elif action == 1: # stand
        state[0].config(text="You: Stand")
    elif action == -1: # clear
        state[0].config(text="You: ")

def updateDealerAction(action, state=[None]):
    if state[0] is None:
        state[0] = action
    elif action == 0: # draw
        state[0].config(text="Dealer: Draw")
    elif action == 1: # stand
        state[0].config(text="Dealer: Stand")
    elif action == -1: # clear
        state[0].config(text="Dealer: ")

def handleSkip(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, skip):
    draw.destroy()
    skip.destroy()
    updatePlayerAction(1)
    print("You stand...")
    window.after(1000, lambda: nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, True))

def handleDrawCard(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, skip):
    draw.destroy()
    skip.destroy()
    updatePlayerAction(0)
    window.after(1000, lambda: drawCard(pile, playerDeck))
    window.after(1000, lambda: nextRound(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, window, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, False))

def updatePlayerButtons(main, pile, playerDeck, userID, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit): # initialises player buttons for drawing, using trump or standing
    draw = Button(main, text="Draw", font=("Arial", 25), bg="black", fg="white")
    stand = Button(main, text="Stand", font=("Arial", 25), bg="black", fg="white", command=lambda: handleSkip(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, main, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, stand))
    draw.config(command= lambda: handleDrawCard(userID, pile, playerDeck, enemyDeck, playerTDeck, enemyTDeck, playerScore, dealerScore, main, dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit, draw, stand))

    draw.place(relx="0.2", rely="0.3", anchor="w")
    stand.place(relx="0.1", rely="0.3", anchor="w")
    #END updatePlayerButtons

def deleteLabels(playerDeckDisplay, enemyDeckDisplay, playerLimit, dealerLimit):
    playerDeckDisplay.destroy()
    enemyDeckDisplay.destroy()
    playerLimit.destroy()
    dealerLimit.destroy()

def updateDeck(playerDeck, enemyDeck, enemyDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit): # updates the display for both decks
    enemyCards = "(???)  "
    playerCards = ""

    for i in range(1, len(enemyDeck)):
        temp = enemyCards
        enemyCards = temp + "(" + enemyDeck[i].symbol + " | " + str(enemyDeck[i].value) + ")  "
    for j in range(len(playerDeck)):
        temp = playerCards
        playerCards = temp + "(" + playerDeck[j].symbol + " | " + str(playerDeck[j].value) + ")  "

    playerDeckDisplay.config(text=playerCards)
    enemyDeckDisplay.config(text=enemyCards)
    playerLimit.config(text=(str(getTotal(playerDeck)) + "/" + str(updateLimit())))
    dealerLimit.config(text=("? + " + str(getTotal(enemyDeck) - enemyDeck[0].value) + "/" + str(updateLimit())))
    #END updateDeck 

def initDeck(main, playerDeck, enemyDeck):
    enemyCards = "(???)  "
    playerCards = ""

    for i in range(1, len(enemyDeck)):
        temp = enemyCards
        enemyCards = temp + "(" + enemyDeck[i].symbol + " | " + str(enemyDeck[i].value) + ")  "
    for j in range(len(playerDeck)):
        temp = playerCards
        playerCards = temp + "(" + playerDeck[j].symbol + " | " + str(playerDeck[j].value) + ")  "

    dealerDeckDisplay = Label(main, text=enemyCards, font=("Arial", 20), bg="black", fg="white", wraplength=1100)
    dealerLimit = Label(main, text=("? + " + str(getTotal(enemyDeck) - enemyDeck[0].value) + "/" + str(updateLimit())), font=("Arial", 20), bg="black", fg="white")
    playerDeckDisplay = Label(main, text=playerCards, font=("Arial", 20), bg="black", fg="white", wraplength=1100)
    playerLimit = Label(main, text=(str(getTotal(playerDeck)) + "/" + str(updateLimit())), font=("Arial", 20), bg="black", fg="white")
    
    dealerDeckDisplay.place(relx="0.6", rely="0.3", anchor="n")
    dealerLimit.place(relx="0.6", rely="0.15", anchor="n")
    playerDeckDisplay.place(relx="0.6", rely="0.9", anchor="s")
    playerLimit.place(relx="0.6", rely="0.75", anchor="s")

    return dealerDeckDisplay, playerDeckDisplay, dealerLimit, playerLimit

def create(userID): # create the main window for the game
    WIDTH = 1200
    HEIGHT = 700
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.title("Game")
    main.config(bg="black")

    dealerTitle = Label(main, text="Dealer", font=("Arial", 20), bg="black", fg="white")
    playerTitle = Label(main, text="Player", font=("Arial", 20), bg="black", fg="white")

    playerAction = Label(main, text="You: ", font=("Arial", 20), bg="black", fg="white")
    dealerAction = Label(main, text="Dealer: ", font=("Arial", 20), bg="black", fg="white")

    scoreLabel = Label(main, text="You: ", font=("Arial", 20), bg="black", fg="white")

    dealerTitle.place(relx="0.6", rely="0.1", anchor="n")
    playerTitle.place(relx="0.6", rely="0.7", anchor="s")

    dealerAction.place(relx="0.3", rely="0.4", anchor="n")
    playerAction.place(relx="0.3", rely="0.5", anchor="s")

    scoreLabel.place(relx="0.2", rely="0.8", anchor="w")

    main.after(100, lambda: updateDealerAction(dealerAction))
    main.after(100, lambda: updatePlayerAction(playerAction))
    main.after(100, lambda: updateScores(0, 0, scoreLabel))
    main.after(1000, lambda: init(userID, 0, 0, main)) # schedule init to run after creating main game window
    main.mainloop()
    #END create

