import sqlite3 as db
from math import trunc

class Voter:
    def __init__(self, iitNumber = "",  fName = "", lName = ""):
        self.iitNumber = iitNumber
        self.fName = fName
        self.lName = lName

    def save(self):
        sql = "INSERT INTO voter (iitNumber, fName, lName) VALUES (?, ?, ?)"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitNumber, self.fName, self.lName))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT iitNumber, fName, lName FROM voter WHERE iitNumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitNumber,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.iitNumber = row[0]
        self.fName = row[1]
        self.lName = row[2]
        return True

    def delete(self):
        sql = "DELETE FROM voter WHERE iitNumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitNumber,))
        con.commit()
        cur.close()
        con.close()
        return True

    def update(self):
        sql = "UPDATE voter SET fName = ? WHERE iitNumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.fName, self.iitNumber))
        con.commit()
        cur.close()
        con.close()
        return True