import os.path

from User import User

FILE_NAME = "users.txt"


def getUser(text):
    parts = text.split('\"')
    if len(parts) == 7:
        testText = parts[0].strip() + parts[2].strip() + parts[4].strip() + parts[6].strip()
        if testText == "":
            user = User()
            user.ID = parts[1]
            user.Name = parts[3]
            user.Phone = parts[5]
            return user
    return None


users = []


def fetchUsers():
    if not os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "x")
        file.close()

    file = open(FILE_NAME, "r")
    for line in file:
        user = getUser(line)
        if user != None:
            users.append(user)
    file.close()


def addUser():
    user = User()

    if len(users) == 0:
        user.ID = 1
    else:
        lastUser = users[len(users) - 1]
        user.ID = int(lastUser.ID) + 1

    name = ""
    while 1:
        name = input("Type user name: ")
        if not name.__contains__('\"'):
            break
        print('User name shouldn\'t contain \" character, please try again!!')
    user.Name = name
    del name

    phone = ""
    while 1:
        phone = input("Type user phone: ")
        if not phone.__contains__('\"'):
            break
        print('User phone shouldn\'t contain \" character, please try again!!')
    user.Phone = phone
    del phone

    out = open(FILE_NAME, "a")
    out.write("\n" + user.toString())
    out.close()
    users.append(user)
    print("User has been added\n")


def searchByID():
    id = int(input("Type user ID: "))
    for user in users:
        if user.ID == id:
            print(user)
            print("")
            return
    print ("User wasn't found\n")


def searchByName():
    name = input("Type user name: ")
    for user in users:
        if user.Name == name:
            print(user)
            print("")
            return
    print ("User wasn't found\n")


def searchByPhone():
    phone = input("Type user phone: ")
    for user in users:
        if user.Phone == phone:
            print(user)
            print("")
            return
    print ("User wasn't found\n")

def printUsers():
    for user in users:
        print(user)
    print("")

fetchUsers()

while 1:
    print("(A) to Add new user, (D) to display users, (I) to search by ID, (N) to search by Name, (P) to search by Phone, (Q) to exit")
    choice = input().strip().lower()

    if choice == 'a':
        addUser()
    elif choice == "i":
        searchByID()
    elif choice == 'n':
        searchByName()
    elif choice == 'p':
        searchByPhone()
    elif choice == "d":
        printUsers()
    else:
        break
