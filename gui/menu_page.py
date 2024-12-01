"""
menu_page.py

Methods that deal with all operations linked to the main menu
"""

#dependencies
from tkinter import *
from userstats import viewStats

def play(userID):
    pass

def rules(main, userID):
    rules = Toplevel(main)
    pass

def stats(main, userID):
    stats = Toplevel(main)
    pass

def create(userID): # create main window
    WIDTH = 1000
    HEIGHT = 500
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.config(bg="black")
    main.title("Main Menu")

    menu = Menu(main)
    main.config(menu=menu)

    header = Label(main, text="Main Menu", font=("Arial", 40), bg="black", fg="white")

    play = Button(main, text="Play Against Dealer", font=("Arial", 30), bg="black", fg="white")
    stats = Button(main, text="View Statistics", font=("Arial", 30), bg="black", fg="white")
    rules = Button(main, text="Rules", font=("Arial", 30), bg="black", fg="white")

    header.place(relx=0.5, rely=0.1, anchor='n')
    play.place(relx=0.5, rely=0.4, anchor=CENTER)
    stats.place(relx=0.5, rely=0.6, anchor=CENTER)
    rules.place(relx=0.5, rely=0.8, anchor=CENTER)

    main.mainloop()
    #END create
