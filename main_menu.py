"""
main_menu.py

This module contains all the methods related to the menu for the game.
"""


# dependencies
import time
from userstats import viewStats

def menu(userID): # lets the user navigate between the different options
    print("\nWelcome to blackjack!")
    navigating = True
    while (navigating):
        nav = int(input("\nWhat would you like to do?\n0 - Play\n1 - Stats\n2 - Rules\n3 - Exit\nYou: "))
        match nav:
            case 0: # Play
                navigating = False
                return
            case 1: # Stats
                viewStats(userID)
            case 2:  # Rules
                rules()
            case 3: 
                navigating = False 
                exit()
    #END menu

def rules(): # prints the rules of blackjack
        print("\n1. You and the dealer will always start off with 2 random cards in your deck, where your first card will always be hidden to your opponent(same goes for dealer).")
        time.sleep(3)
        print("2. You must either draw a card, or pass - If you choose to draw a card, you will be given a random card from 1 to 11 that will be added to your deck. If you pass, you will skip to the dealers turn.")
        time.sleep(3)
        print("3. The goal of the game is to draw cards until you get a sum up to 21 - However, going above this limit limits your turn to a pass and a win for the dealer, and vice versa.")
        time.sleep(3)
        print("4. If both parties pass, then this result in a showdown, where the 'judge' compares the total points of both decks, and the player closest to 21 is the winner!")
        time.sleep(3)
        print("5. However, it should be noted that if you get the same points as the dealer, this will not result in a draw, rather a loss for you.")
        time.sleep(2)
        print("6. First to 3 wins is declared as the winner.")
        time.sleep(2)
    #END rules