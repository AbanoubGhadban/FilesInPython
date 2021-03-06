import os.path

import FileOperations
from User import User

currentUser = User()

def addUser():
    user = getUserData()
    user.ID = FileOperations.getNextId()

    FileOperations.addUser(user)
    print("User has been added\n")


def searchByID():
    id = int(input("Type user ID: "))
    user = FileOperations.getUserById(id)

    if user == None:
        print("User wasn't found\n")
    else:
        print(user)
        modifyUser(user)


def searchByName():
    name = input("Type user name: ")
    user = FileOperations.getUserByName(name)

    if user == None:
        print("User wasn't found\n")
    else:
        print(user)
        modifyUser(user)


def searchByPhone():
    phone = input("Type user phone: ")
    user = FileOperations.getUserByPhone(phone)

    if user == None:
        print ("User wasn't found\n")
    else:
        print(user)
        modifyUser(user)

def searchByEmail():
    email = input("Type user E-mail: ")
    user = FileOperations.getUserByEmail(email)

    if user == None:
        print ("User wasn't found\n")
    else:
        print(user)
        modifyUser(user)

def printUsers():
    users = FileOperations.getUsers(0, FileOperations.getNumberOfUsers())
    print("{0:12}{1:32}{2:32}{3:32}".format('ID', 'Name', 'Phone', 'E-mail'))
    for user in users:
        print(user.getPrintableUser())
    print("")

def getUserData():
    user = User()

    user.Name = input("Type user name: ")
    user.Phone = input("Type user phone: ")
    user.Email = input("Type user e-mail: ")
    return user

def modifyUserData(user):
    print("Type user data in each field (Type nothing in field you don't want to modify)")

    name = input("Type user name: ")
    if name.strip() != '':
        user.Name = name

    phone = input("Type user phone: ")
    if phone.strip() != '':
        user.Phone = phone

    email = input("Type user e-mail: ")
    if email.strip() != '':
        user.Email = email

def modifyUser(user):
    print("Type (M) to modify user data, (D) to delete user")

    inp = input().lower().strip()
    if inp == 'm':
        modifyUserData(user)

        FileOperations.modifyUserData(user)
        print('User has been modified\n')
    elif inp == 'd':
        if input("Are you sure you want to delete user ?? (Y/N): ").lower().strip() == 'y':
            FileOperations.deleteUser(user)
            print("User has been deleted\n")

while 1:
    print("(A) to Add new user, (D) to display users, (I) to search by ID, (N) to search by Name, (P) to search by Phone, (E) to search by E-mail, (Q) to exit")
    choice = input().strip().lower()

    if choice == 'a':
        addUser()
    elif choice == "i":
        searchByID()
    elif choice == 'n':
        searchByName()
    elif choice == 'p':
        searchByPhone()
    elif choice == 'e':
        searchByEmail()
    elif choice == "d":
        printUsers()
    else:
        break
