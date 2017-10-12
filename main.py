import os.path


FILE_NAME = "users.txt"


def getUser(text):
    text = text.strip()
    user = User()
    par = getData(text)
    if par[0] == "":
        return None

    user.ID = par[0]
    text = par[1].strip()

    par = getData(text)
    user.Name = par[0]
    text = par[1].strip()

    par = getData(text)
    user.Phone = par[0]
    return user


def getData(text):
    if text == "":
        return ["", ""]

    if text[0] == "\"":
        length = len(text)
        i = 0
        while 1:
            i += 1
            if i > (length - 1):
                return [text[1:], ""]

            if text[i] == "\"":
                return [text[1:i], text[i + 1:]]
            elif text[i] == "\n":
                return ["", text[i + 1:]]
    return ["", ""]


class User:
    def __init__(self, ID="", Name="", Phone=""):
        self.ID = ID
        self.Name = Name
        self.Phone = Phone

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, value):
        self._Phone = value

    def __repr__(self):
        return "ID: {0}, Name: {1}, Phone: {2}".format(self.ID, self.Name, self.Phone)

    def toString(self):
        return "\"{0}\" \"{1}\" \"{2}\"".format(self.ID, self.Name, self.Phone)


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

    user.Name = input("Type user name: ")
    user.Phone = input("Type user phone: ")

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
