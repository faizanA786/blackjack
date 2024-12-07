"""
init.py

The root of the program.
This is called upon launching the program.
"""

# dependencies
from gui import init_page
from gui import login_page
from gui import menu_page
from userstats import dbInit
import game

def init(): # initialises the program and directs flow
    dbInit() # init database
    init_page.create() # login
    userID = login_page.fetchUserID()
    menu_page.create(userID) # main menu
    game.init(userID)
    #END init

init()