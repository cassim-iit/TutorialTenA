import sqlite3 as db


def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS voter(iitNumber int(8) PRIMARY KEY, fName varchar(10), lName varchar(10))"
    con = db.connect("database\\voter.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

initializeDatabase()