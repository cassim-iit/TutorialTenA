import sqlite3 as db

class Committee:
    def __init__(self, committee_id, committee_name):
        self.committee_id = committee_id
        self.committee_name = committee_name

    def save(self):
        sql = "INSERT INTO committee(name,) VALUES (?, ?)"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.username, self.password))
        con.commit()
        cur.close()
        con.close()