import new_card as nc
import time

def navigate(playerDeck, enemyDeck):
    nav = int(input("\n0 - Draw\n1 - Pass\n2 - Use Trump Card\n3 - View Deck\nYou: "))
    match nav:
        case 0: # Draw
            playerSum = 0
            for i in range(len(playerDeck)):
                playerSum += playerDeck[i].value
            if playerSum < 21:
                return drawCard(playerDeck)
            else:
                print("\nYou cannot draw a card! You are above 21!")
                return navigate(playerDeck, enemyDeck)
        case 1: # Stand
            print("\nYou stand...")
            return True
        case 2: # Trump Card
            pass
        case 3: # View
            deck = int(input("\n0 - Your deck\n1 - Dealer Deck\nYou: "))
            viewCard(deck, playerDeck, enemyDeck)
            navigate(playerDeck, enemyDeck)

def drawCard(playerDeck):
    print("\nYou draw a card...")
    time.sleep(1)
    newCard = nc.newCard()
    print("You were dealt a " + str(newCard.value) + " " + newCard.symbol)
    playerDeck.append(newCard)
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