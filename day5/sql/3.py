import sqlite3

objcon = sqlite3.connect('sports.db')
objcur = objcon.cursor()

query = """INSERT into players
        (id, name, skill, price)
        VALUES(?,?,?,?)"""

lista = [2, "deepika", "archery", 23400]
listb = [4, "sushil", "wrestler", 32000]
listc = [6, "mithali", "cricket", 42000]
listd = [8, "vishwanath", "chess", 34000]

objcur.execute(query, lista)
objcon.commit()
objcon.close()
