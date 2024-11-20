"""
init.py

The root of the program.
This is called upon launching the program.
"""

# dependencies
from tkinter import *
from userstats import dbInit, newProfile, login 
import main_menu
import game

def init(): # initialises the program
    WIDTH = 1000
    HEIGHT = 500
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.config(bg="black")
    main.title("Main Menu")

    menu = Menu(main)
    main.config(menu=menu)

    header = Label(main, text="Blackjack!", font=("Arial", 40), bg="black", fg="white")
    #createProfile = Button(main, text="New Profile", font=("Arial", 30), bg="black", fg="white", command=)
    #login = Button(main, text="Login", font=("Arial", 30), bg="black", fg="white", command=)
    exit = Button(main, text="Exit", font=("Arial", 30), bg="black", fg="white", command=main.destroy)

    header.place(relx=0.5, rely=0.2, anchor=CENTER)
    #createProfile.place()
    #login.place()
    exit.place(relx=0.5, rely=0.6, anchor=CENTER)
    main.mainloop()

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