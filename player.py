import new_card as nc
import game_utils as u
import time

def navigate(playerDeck, enemyDeck, playerTDeck):
    deciding = True
    while deciding:
        nav = int(input("\n0 - Draw\n1 - Pass\n2 - Use Trump Card\n3 - View Deck\nYou: "))
        match nav:
            case 0: # Draw
                playerSum = u.getTotal(playerDeck)
                if playerSum < u.updateLimit():
                    deciding = False
                    drawCard(playerDeck)
                    return False
                else:
                    print("\nYou cannot draw a card! You are above " + str(u.updateLimit()) + "!")
            case 1: # Stand
                deciding = False
                print("\nYou stand...")
                return True
            case 2: # Trump Card
                useTrump(playerDeck, enemyDeck, playerTDeck)
            case 3: # View
                deck = int(input("\n0 - Your deck\n1 - Dealer Deck\nYou: "))
                viewCard(deck, playerDeck, playerTDeck, enemyDeck)

def drawCard(playerDeck):
    print("\nYou draw a card...")
    time.sleep(1)
    newCard = nc.newCard()
    print("You were dealt a " + str(newCard.value) + " " + newCard.symbol)
    playerDeck.append(newCard)
    return

def useTrump(playerDeck, enemyDeck, playerTDeck):
    if len(playerTDeck) > 0:
        print("\nYour trump cards:")
        time.sleep(1)
        for i in range(len(playerTDeck)):
            print("(" + str(playerTDeck[i].trumpVal) + ")" + " - " + str(playerTDeck[i].name) + " : " + str(playerTDeck[i].desc))
    trumpVal = int(input("\nEnter the value associated with the card to use it (x), or return to navigation (-1)\nYou: "))
    if u.getTrump(trumpVal, playerTDeck): 
        print("\nYou used a trump card!")
        u.useTrump(trumpVal)
        return
    elif trumpVal == -1:
        return
    elif u.getTrump(trumpVal, playerTDeck) == False:
        print("You do not have this trump card")
        return

def viewCard(deck, playerDeck, playerTDeck, enemyDeck):
    if deck == 0:
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
    
    elif deck == 1:
        print("\nEnemy deck:")
        for i in range(len(enemyDeck)):
            if i == 0:
                print("???")
            else:
                print(str(enemyDeck[i].value) + " " + str(enemyDeck[i].symbol))
        print("x + " + str(u.getTotal(enemyDeck) - enemyDeck[0].value) + " /" + str(u.updateLimit(None)))
        time.sleep(1)
        return
    
