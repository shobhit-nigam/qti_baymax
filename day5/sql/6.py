import sqlite3
import pandas as pd

objcon = sqlite3.connect('sports.db')
query = """SELECT * FROM players"""
dfa = pd.read_sql(query, objcon)

dfa.to_excel("players.xlsx", index=False)
objcon.close()
