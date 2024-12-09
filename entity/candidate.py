import sqlite3 as db
from math import trunc

class Candidate:
    def __init__(self, candidateName = "",  candidateNumber = "", candidateHouse=""):
        self.candidateName = candidateName
        self.candidateNumber = candidateNumber
        self.candidateHouse = candidateHouse


    def save(self ):
        sql = "INSERT INTO candidate (candidateName, candidateNumber,candidateHouse) VALUES (?, ?,?)"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidateName, self.candidateNumber,self.candidateHouse))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT candidateName,candidateNumber,candidateHouse FROM user WHERE candidateName = ?"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidateName,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.candidateName = row[0]
        self.candidateNumber = row[1]
        self.candidateHouse = row[2]
        return True

    def delete(self):
        sql = "DELETE FROM candidate WHERE userName = ?"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidateName,))
        con.commit()
        cur.close()
        con.close()
        return True

    def update(self):
        sql = "UPDATE candidate SET candidateNumber = ? WHERE candidateHouse = ?"
        con = db.connect("database\\candidate.db")
        cur = con.cursor()
        cur.execute(sql, (self.candidateNumber, self.candidateHouse))
        con.commit()
        cur.close()
        con.close()
        return True