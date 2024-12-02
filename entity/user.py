import sqlite3 as db
from math import trunc

class User:
    def __init__(self, username = "",  password = ""):
        self.username = username
        self.password = password

    def save(self):
        sql = "INSERT INTO user (userName, passWord) VALUES (?, ?)"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username, self.password))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT userName,passWord FROM user WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.username = row[0]
        self.password = row[1]
        return True

    def delete(self):
        sql = "DELETE FROM user WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username,))
        con.commit()
        cur.close()
        con.close()
        return True

    def update(self):
        sql = "UPDATE user SET passWord = ? WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.password, self.username))
        con.commit()
        cur.close()
        con.close()
        return True