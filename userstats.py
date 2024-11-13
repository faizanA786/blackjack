import sqlite3 as sq
import time

def dbInit():
    connectDatabase = sq.connect("user.db")
    database = connectDatabase.cursor()

    database.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            games INTEGER DEFAULT 0,
            games_won INTEGER DEFAULT 0,
            games_lost INTEGER DEFAULT 0
            )
        '''
    )

    database.execute("SELECT * FROM users")
    users = database.fetchall()
    print(users)

    connectDatabase.commit()
    connectDatabase.close()

def newProfile(username, password):
    connectDatabase = sq.connect("user.db")
    database = connectDatabase.cursor()

    database.execute("SELECT user_id FROM users WHERE username = ?", (username,))
    userID = database.fetchone()
    if userID is not None:
        print("This username already exists!")
        connectDatabase.close()
    else:
        print("New profile created!")
        database.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connectDatabase.commit()

        database.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        userID = database.fetchone()
        connectDatabase.close()
        return userID[0]

def login(username, password):
    connectDatabase = sq.connect("user.db")
    database = connectDatabase.cursor()

    database.execute("SELECT user_id FROM users WHERE username = ? AND password = ?", (username, password))
    userID = database.fetchone()
    if userID is None:
        print("That username or password is incorrect!")
        connectDatabase.close()
    else:
        print("Logged in!")
        connectDatabase.close()
        return userID[0]

def updateStats(userID, stats):
    connectDatabase = sq.connect("user.db")
    database = connectDatabase.cursor()

    database.execute("UPDATE users SET games = games + 1 WHERE user_id = ?", [userID])
    match stats:
        case 0: # Win
            database.execute("UPDATE users SET games_won = games_won + 1 WHERE user_id = ?", [userID])
            connectDatabase.commit()
        case 1: # Lose
            database.execute("UPDATE users SET games_lost = games_lost + 1 WHERE user_id = ?", [userID])
            connectDatabase.commit()
    connectDatabase.close()

def viewStats(userID):
    connectDatabase = sq.connect("user.db")
    database = connectDatabase.cursor()

    database.execute("SELECT games, games_won, games_lost FROM users WHERE user_id = ?", [userID])
    stats = database.fetchone()

    time.sleep(1)
    print("\nGames played : " + str(stats[0]))
    print("Wins : " + str(stats[1]))
    print("Losses : " + str(stats[2]))
    connectDatabase.close()
    time.sleep(1)