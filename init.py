"""
init.py

The root of the program.
This is called upon launching the program.
"""

# dependencies
from tkinter import *
from userstats import dbInit, newProfile, login as existingProfile
import main_menu
import game

def enterProfile(main, type): # type = 0 = new profile / type = 1 = existing profile
    WIDTH = 500
    HEIGHT = 400
    login = Toplevel(main)
    login.geometry(str(WIDTH) + "x" + str(HEIGHT))
    login.config(bg="black")
    login.title = "Create Profile"

    if type == 0:
        title = "Create Profile"
    elif type == 1:
        title = "Login"

    header = Label(login, text=title, font=("Arial", 20), bg="black", fg="white")
    username = Label(login, text="Username: ", font=("Arial", 15), bg="black", fg="white")
    password = Label(login, text="Password: ", font=("Arial", 15), bg="black", fg="white")
    invalid = Label(login, text="Invalid!", font=("Arial", 20), bg="black", fg="red")

    usernameEntry = Entry(login, font=("Arial", 15), bg="black", fg="white", insertbackground="white")
    passwordEntry = Entry(login, font=("Arial", 15), bg="black", fg="white", insertbackground="white")
    
    def getUserID(type):
        if type == 0:
            userID = newProfile(usernameEntry.get(), passwordEntry.get())
        elif type == 1:
            userID = existingProfile(usernameEntry.get(), passwordEntry.get())
        if userID is None:
                usernameEntry.delete(0, END)
                passwordEntry.delete(0, END)
                invalid.place(relx=0.7, rely=0.85, anchor="w")
        else:
            login.destroy()
            main.destroy()
            main_menu.menu(userID)

    submit = Button(login, text=title, font=("Arial", 20), bg="black", fg="white", command=lambda: getUserID(type))

    header.place(relx=0.5, rely=0.2, anchor=CENTER)
    username.place(relx=0.2, rely=0.4, anchor="w")
    password.place(relx=0.2, rely=0.6, anchor="w")
    usernameEntry.place(relx=0.45, rely=0.4, anchor="w")
    passwordEntry.place(relx=0.45, rely=0.6, anchor="w")
    submit.place(relx=0.5, rely=0.9, anchor="s")

    main.withdraw() 

    def close():
        main.deiconify()  
        login.destroy()   

    login.protocol("WM_DELETE_WINDOW", close)

    login.grab_set()
    login.mainloop()

def init(): # initialises the program
    dbInit()

    WIDTH = 1000
    HEIGHT = 500
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.config(bg="black")
    main.title("Main Menu")

    menu = Menu(main)
    main.config(menu=menu)

    header = Label(main, text="Blackjack!", font=("Arial", 40), bg="black", fg="white")

    newProfile = Button(main, text="New Profile", font=("Arial", 30), bg="black", fg="white", command=lambda: enterProfile(main, 0))
    existingProfile = Button(main, text="Login", font=("Arial", 30), bg="black", fg="white", command=lambda: enterProfile(main, 1))

    header.place(relx=0.5, rely=0.2, anchor=CENTER)
    newProfile.place(relx=0.5, rely=0.4, anchor=CENTER)
    existingProfile.place(relx=0.5, rely=0.6, anchor=CENTER)

    main.mainloop()




    # dbInit()
    # nav = int(input("Login (0)\nNew Account (1)\nYou: "))
    # signedIn = False
    # while not signedIn:
    #     username, password = loginDetails()
    #     match nav:
    #         case 0:
    #             userID = login(username, password)
    #             if userID is not None:
    #                 signedIn = True
    #         case 1:
    #             userID = newProfile(username, password)
    #             if userID is not None:
    #                 signedIn = True
    # main_menu.menu(userID)
    # game.init(userID)
    #END init

# def loginDetails(): # fetches user input for username and password
#     username = input("Username: ")
#     password = input("Password: ")
#     return username, password
#     #END loginDetails

init()