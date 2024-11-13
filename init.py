from userstats import dbInit, newProfile, login 
import main_menu
import game

def init():
    dbInit()
    nav = int(input("Login (0)\nNew Account (1)\nYou: "))
    signedIn = False
    while not signedIn:
        username, password = loginDetails()
        match nav:
            case 0:
                userID = login(username, password)
                if userID is not None:
                    signedIn = True
            case 1:
                userID = newProfile(username, password)
                if userID is not None:
                    signedIn = True
    main_menu.menu(userID)
    game.init(userID)

def loginDetails():
    username = input("Username: ")
    password = input("Password: ")
    return username, password

init()