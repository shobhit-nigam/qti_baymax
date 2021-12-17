import sqlite3

objcon = sqlite3.connect('sports.db')
objcur = objcon.cursor()

query = """CREATE TABLE players(id integer PRIMARY KEY,
        name text,
        skill text,
        price real)"""

objcur.execute(query)
objcon.close()
