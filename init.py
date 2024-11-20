"""
init.py

The root of the program.
This is called upon launching the program.
"""

# dependencies
from userstats import dbInit, newProfile, login 
import main_menu
import game

def init(): # initialises the program
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
    #END init

def loginDetails(): # fetches user input for username and password
    username = input("Username: ")
    password = input("Password: ")
    return username, password
    #END loginDetails

init()