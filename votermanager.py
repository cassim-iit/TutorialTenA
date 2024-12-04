import sqlite3 as db
from entity.voter import Voter

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
    oVoter = Voter()
    oVoter.iitNumber = iitNumber
    oVoter.fName = fName
    oVoter.lName = lName
    oVoter.update()

def getAllVoters():
    oVoters = []
    sql = "SELECT iitNumber, fName, lName FROM voter"
    con = db.connect("database\\voter.db")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    for row in rows:
        oVoter = Voter()
        oVoter.iitNumber = row[0]
        oVoter.fName = row[1]
        oVoter.lName = row[2]
        oVoters.append(Voter)
    return Voters

def printVoterList(oVoter):
    for oVoter in oVoter:
        print(oVoter.iitNumber, oVoter.fName, oVoter.lName)

def menu():
    x = 0;
    while (x != 9):
        print("1. Show all voters\n"
              "2. Add new voter\n"
              "3. Remove voter\n"
              "4. Update voter\n"
              "9. Exit")
        x = int(input("Enter your choice: "))
        match x:
            case 1:
                oList = getAllVoters()
                printVoterList(oList)
            case 2:
                iitNumber = int(input("Enter your iitNumber: "))
                fName = input("Enter your first name: ")
                lName = input("Enter your last name: ")
                insertVoter(iitNumber, fName, lName)
                print("Voter added successfully")
            case 3:
                iitNumber = input("Enter your iitNumber: ")
                removeVoter(iitNumber)
                print("Voter removed successfully")
            case 4:
                iitNumber = int(input("Enter your iitNumber: "))
                fName = input("Enter your first name: ")
                lName = input("Enter your last name: ")
                updateVoter(iitNumber, fName, lName)
                print("User updated successfully")

#main for this module
initializeDatabase()
menu()