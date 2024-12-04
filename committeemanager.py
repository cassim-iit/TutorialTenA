import sqlite3 as db

def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS committee( Com_id TEXT PRIMARY KEY, name TEXT, age int, address TEXT )"
    con = db.connect("database\\committee.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

initializeDatabase()

