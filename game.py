import new_card as nc
import time
import os

def init():
    playerDeck = [nc.newCard(), nc.newCard()]
    enemyDeck = [nc.newCard(), nc.newCard()]
    viewCard(0, playerDeck, enemyDeck)
    viewCard(1, playerDeck, enemyDeck)
    navigate(playerDeck, enemyDeck)

def navigate(playerDeck, enemyDeck):
    nav = int(input("\n0 - Draw\n1 - Pass\n2 - Use Trump Card\n3 - View Deck\nYou: "))
    match nav:
        case 0:
            drawCard(playerDeck)
            navigate(playerDeck, enemyDeck)
        case 1:
            pass
        case 2:
            pass
        case 3:
            deck = int(input("\n0 - Your deck\n1 - Dealer Deck\nYou: "))
            viewCard(deck, playerDeck, enemyDeck)
            navigate(playerDeck, enemyDeck)

def drawCard(playerDeck):
    time.sleep(1)
    newCard = nc.newCard()
    print("\nYou were dealt a " + str(newCard.value) + " " + newCard.symbol)
    playerDeck.append(newCard)
    viewCard(0, playerDeck, None)
    return

def viewCard(deck, playerDeck, enemyDeck):
    sum = 0
    if deck == 0:
        time.sleep(1)
        print("\nYour hand:")
        for i in range(len(playerDeck)):
            print(str(playerDeck[i].value) + " " + str(playerDeck[i].symbol))
            sum += playerDeck[i].value
        print(str(sum) + "/21")
        time.sleep(1)
        return
    
    elif deck == 1:
        time.sleep(1)
        print("\nEnemy deck:")
        for i in range(len(enemyDeck)):
            if i == 0:
                print("???")
            else:
                print(str(enemyDeck[i].value) + " " + str(enemyDeck[i].symbol))
                sum += enemyDeck[i].value
        print("x + " + str(sum) + " /21")
        time.sleep(1)
        return

init()