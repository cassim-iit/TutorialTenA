import sqlite3 as db
from entity.candidate import Candidate

def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS candidate(candidateName TEXT PRIMARY KEY,candidateNumber Text,candidateHouse TEXT )"
    con = db.connect("database\\candidate.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def insertCandidate(candidateName, CandidateNumber, CandidateHouse):
    oCandidate = Candidate()
    oCandidate.candidateName = candidateName
    oCandidate.CandidateNumber = CandidateNumber
    oCandidate.CandidateHouse = CandidateHouse

    oCandidate.save()

def removeCandidate(candidateName):
    oCandidate = Candidate()
    oCandidate.candidateName = candidateName
    oCandidate.delete()

def updateCandidate(candidateName, CandidateNumber, CandidateHouse):
    oCandidate = Candidate()
    oCandidate.candidateName =candidateName
    oCandidate.CandidateNumber = CandidateNumber
    oCandidate.CandidateHouse = CandidateHouse
    oCandidate.update()

def getCandidate(candidateName):
    oCandidate = Candidate()
    oCandidate.candidateName =candidateName
    oCandidate.load()
    return oCandidate

def getAllCandidates():
    oCandidate = []
    sql = "SELECT candidateName, CandidateNumber, CandidateHouse FROM candidate"
    con = db.connect("database\\candidate.db")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    for row in rows:
        oCandidate = Candidate()
        oCandidate.candidateName = row[0]
        oCandidate.candidateNumber = row[1]
        oCandidate.candidateHouse = row[2]
        oCandidate.append(oCandidate)
    return True

def printCandidateList(oCandidate):
    for oCandidate in oCandidate:
        print(oCandidate.CandidateName, oCandidate.CandidateNumber)


def menu():
    x = 0;
    while (x != 9):
        print("1. Show all candidates\n"
              "2. Add new candidate\n"
              "3. Remove candidate\n"
              "4. Update candidate\n"
              "9. Exit")
        x = int(input("Enter your choice: "))
        match x:
            case 1:
                oList = getAllCandidates()
                printCandidateList(oList)
            case 2:
                candidateName = input("Enter your name: ")
                candidateNumber = input("Enter your number: ")
                candidateHouse = input("Enter your house: ")
                insertCandidate(candidateName, candidateNumber,candidateHouse)
                print("candidate added successfully")
            case 3:
                candidateNameName = input("Enter your candidate name: ")
                removeCandidate(candidateNameName)
                print("User removed successfully")
            case 4:
                candidateName = input("Enter your Name: ")
                candidateNumber = input("Enter your number: ")
                candidateHouse = input("Enter your house: ")

                updateCandidate(candidateName, candidateNumber,candidateHouse)
                print("candidate updated successfully")

#main for this module
initializeDatabase()
menu()