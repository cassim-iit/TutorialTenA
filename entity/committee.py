import sqlite3 as db

class Committee:
    def __init__(self, committee_id, committee_name, age, address):
        self.committee_id = committee_id
        self.committee_name = committee_name
        self.age = age
        self.address = address

    def save(self):
        sql = "INSERT INTO committee(Com_id,name,age,address) VALUES (?, ?,?,?)"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committee_id, self.committee_name, self.age, self.address))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT * FROM committee WHERE userName = ?"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.username,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.committee_id = row[0]
        self.username = row[1]
        self.age = row[2]
        self.address = row[3]
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

    def updateName(self, newname):
        sql = "UPDATE user SET com_id=? WHERE userName = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.committee_id, newname))
        con.commit()
        cur.close()
        con.close()
        return True