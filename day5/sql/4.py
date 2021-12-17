import sqlite3

objcon = sqlite3.connect('sports.db')
objcur = objcon.cursor()

query = """INSERT into players
        (id, name, skill, price)
        VALUES(?,?,?,?)"""

listb = [4, "sushil", "wrestler", 32000]
listc = [6, "mithali", "cricket", 42000]
listd = [8, "vishwanath", "chess", 34000]

listx = [listb, listc, listd]

objcur.executemany(query, listx)
objcon.commit()
objcon.close()
