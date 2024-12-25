"""
player.py

The module that controls the functionality of you, as the player.
Controls the functionality of using a trump, stand or draw a card.
"""

# dependencies
from gui import game_page
import new_card as nc
import game_utils as u
import time

def drawCard(pile, playerDeck): # draws a random card from the pile into your deck
    print("\nYou draw a card...")
    newCard = pile.pop()
    print("You were dealt a " + str(newCard.value) + " " + newCard.symbol)
    playerDeck.append(newCard)
    #END drawCard

def useTrump(pile, playerDeck, playerTDeck): # uses a trump card
    if len(playerTDeck) > 0:
        print("\nYour trump cards:")
        for i in range(len(playerTDeck)):
            print("(" + str(playerTDeck[i].trumpVal) + ")" + " - " + str(playerTDeck[i].name) + " : " + str(playerTDeck[i].desc))

    trumpVal = int(input("\nEnter the value associated with the card to use it (x), or return to navigation (-1)\nYou: "))
    if u.getTrump(trumpVal, playerTDeck): 
        print("\nYou used a trump card!")
        return trumpVal, u.useTrump(trumpVal, pile, playerDeck)
    elif trumpVal == -1:
        return -1, None
    elif u.getTrump(trumpVal, playerTDeck) == False:
        print("You do not have this trump card")
        return -1, None
    #END useTrump
