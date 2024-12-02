""""
https://www.sqlitetutorial.net/sqlite-create-table/
"""
import sqlite3 as db
from entity.user import User


def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS user(userName TEXT PRIMARY KEY, passWord TEXT)"
    con = db.connect("database\\login.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

def insertUser(userName, passWord):
    oUser = User()
    oUser.username = userName
    oUser.password = passWord
    oUser.save()

def removeUser(userName):
    oUser = User()
    oUser.username = userName
    oUser.delete()

def updateUser(userName, passWord):
    oUser = User()
    oUser.username = userName
    oUser.password = passWord
    oUser.update()

def getUser(userName):
    oUser = User()
    oUser.username = userName
    oUser.load()
    return oUser

def getAllUsers():
    oUsers = []
    sql = "SELECT userName, passWord FROM user"
    con = db.connect("database\\login.db")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    for row in rows:
        oUser = User()
        oUser.username = row[0]
        oUser.password = row[1]
        oUsers.append(oUser)
    return oUsers

def printUserList(oUsers):
    for oUser in oUsers:
        print(oUser.username, oUser.password)

def menu():
    x = 0;
    while (x != 9):
        print("1. Show all users\n"
              "2. Add new user\n"
              "3. Remove user\n"
              "4. Update user\n"
              "9. Exit")
        x = int(input("Enter your choice: "))
        match x:
            case 1:
                oList = getAllUsers()
                printUserList(oList)
            case 2:
                userName = input("Enter your username: ")
                passWord = input("Enter your password: ")
                insertUser(userName, passWord)
                print("User added successfully")
            case 3:
                userName = input("Enter your username: ")
                removeUser(userName)
                print("User removed successfully")
            case 4:
                userName = input("Enter your username: ")
                passWord = input("Enter your password: ")
                updateUser(userName, passWord)
                print("User updated successfully")

#main for this module
initializeDatabase()
menu()




