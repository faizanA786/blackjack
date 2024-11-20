"""
player.py

The module that controls the functionality of you, as the player.
Lets you navigate between deciding to use a trump, stand or draw a card.
"""

# dependencies
import new_card as nc
import game_utils as u
import time

def navigate(pile, playerDeck, enemyDeck, playerTDeck): # lets you navigate between drawing, standing or using a trump
    deciding = True
    while deciding:
        nav = int(input("\n0 - Draw\n1 - Pass\n2 - Use Trump Card\n3 - View Deck\nYou: "))
        match nav:
            case 0: # Draw
                playerSum = u.getTotal(playerDeck)
                if playerSum < u.updateLimit():
                    deciding = False
                    drawCard(pile, playerDeck)
                    return False
                else:
                    print("\nYou cannot draw a card! You are above " + str(u.updateLimit()) + "!")
            case 1: # Stand
                deciding = False
                print("\nYou stand...")
                return True
            case 2: # Trump Card
                trumpVal, newDeck = useTrump(pile, playerDeck, playerTDeck)
                match trumpVal:
                    case 2:
                        playerDeck[:] = newDeck
                        # deciding = False
                        # return False
            case 3: # View
                deck = int(input("\n0 - Your deck\n1 - Dealer Deck\nYou: "))
                viewCard(deck, playerDeck, playerTDeck, enemyDeck)
    #END navigate

def drawCard(pile, playerDeck): # draws a random card from the pile into your deck
    print("\nYou draw a card...")
    time.sleep(1)
    newCard = pile.pop()
    print("You were dealt a " + str(newCard.value) + " " + newCard.symbol)
    playerDeck.append(newCard)
    return
    #END drawCard

def useTrump(pile, playerDeck, playerTDeck): # uses a trump card
    if len(playerTDeck) > 0:
        print("\nYour trump cards:")
        time.sleep(1)
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

def viewCard(deck, playerDeck, playerTDeck, enemyDeck): # lets you view your deck or the enemies
    if deck == 0: # you
        print("\nYour hand:")
        for i in range(len(playerDeck)):
            print(str(playerDeck[i].value) + " " + str(playerDeck[i].symbol))
        print(str(u.getTotal(playerDeck)) + " /" +  str(u.updateLimit()))

        if len(playerTDeck) > 0:
            print("\nYour trump cards:")
            time.sleep(1)
            for i in range(len(playerTDeck)):
                print(str(playerTDeck[i].name) + " : " + str(playerTDeck[i].desc))

        time.sleep(1)
        return
    
    elif deck == 1: # dealer
        print("\nDealer deck:")
        for i in range(len(enemyDeck)):
            if i == 0:
                print("???")
            else:
                print(str(enemyDeck[i].value) + " " + str(enemyDeck[i].symbol))
        print("x + " + str(u.getTotal(enemyDeck) - enemyDeck[0].value) + " /" + str(u.updateLimit(None)))
        time.sleep(1)
        return
    #END viewCard
    
