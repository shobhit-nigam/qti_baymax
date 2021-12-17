import sqlite3
import pandas as pd

objcon = sqlite3.connect('sports.db')
query = """SELECT * FROM players"""
dfa = pd.read_sql(query, objcon)

print(dfa)

objcon.close()
