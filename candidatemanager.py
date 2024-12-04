import sqlite3 as db

def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS candidate(candidateName TEXT PRIMARY KEY,candidateNumber Text,candidateHouse TEXT )"
    con = db.connect("database\\candidate.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()