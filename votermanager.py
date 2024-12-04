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

def insertVoter(iitNumber, fName, lName):
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.fName = fName
    oVoter.lName = lName
    oVoter.save()

def removeVoter(iitNumber,):
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.delete()

def updateVoter(iitNumber, fName, lName):
    oUser = Voter()
    oUser.iitNumber = iitNumber
    oUser.fName = fName
    oUser.lName = lName
    oUser.update()
