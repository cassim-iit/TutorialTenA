import sqlite3 as db

def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS committee( Com_id INT(4) PRIMARY KEY, name TEXT, age int(3), address TEXT )"
    con = db.connect("database\\committee.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

def add(name, age, address):
    sql = "INSERT INTO committee VALUES (name, age , address);"
    con= db.connect("database\\committee.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

initializeDatabase()