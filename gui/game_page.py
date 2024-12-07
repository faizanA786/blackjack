"""
game_page.py

Methods that deal with all operations linked to actual gameplay
"""

#dependencies
from tkinter import *

def create(userID):
    WIDTH = 1000
    HEIGHT = 700
    main = Tk()
    main.geometry(str(WIDTH) + "x" + str(HEIGHT))
    main.title("Game")
    main.config(bg="black")