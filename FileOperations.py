import os

import Global
from Global import FILE_NAME, USER_STRING_LENGTH
from User import User

def getNumberOfUsers():
    return int(os.path.getsize(FILE_NAME)/USER_STRING_LENGTH)

def addUser(user):
    f = open(FILE_NAME, 'a')
    f.write(user.toString())
    f.close()

def addUsers(users):
    f = open(FILE_NAME, 'a')
    for user in users:
        f.write(user.toString())
    f.close()

def getUser(index):
    f = open(FILE_NAME, 'r')
    f.seek(index*USER_STRING_LENGTH)
    user = Global.parseUser(f.read(USER_STRING_LENGTH))
    f.close()
    return user

def getUsers(startIndex=0, count=0):
    index = startIndex*USER_STRING_LENGTH
    length = count*USER_STRING_LENGTH

    f = open(FILE_NAME, 'r')
    f.seek(index)
    users = []
    usersData = f.read(length)
    f.close()

    while 1:
        if len(usersData) < USER_STRING_LENGTH:
            return users

        user = Global.parseUser(usersData[:USER_STRING_LENGTH])
        if user != None:
            users.append(Global.parseUser(usersData[:USER_STRING_LENGTH]))
        usersData = usersData[USER_STRING_LENGTH:]

def getUserById(userId):
    index = (int(userId) - 1) * USER_STRING_LENGTH
    if index > os.path.getsize(FILE_NAME) - 1:
        return None

    f = open(FILE_NAME, 'r')
    f.seek(index)
    userData = f.read(Global.USER_STRING_LENGTH)
    user = Global.parseUser(userData)
    f.close()
    return user
    # userId = str(userId).strip()
    # #Number of users in file
    # count = int(os.path.getsize(FILE_NAME)/USER_STRING_LENGTH)
    #
    # f = open(FILE_NAME, 'r')
    #
    # userData = ''
    # i = 0
    # for i in range(count):
    #     f.seek(i*USER_STRING_LENGTH + Global.USER_ID_INDEX)
    #     if f.read(Global.USER_ID_LENGTH).strip() == userId:
    #         f.seek(i*USER_STRING_LENGTH)
    #         userData = f.read(USER_STRING_LENGTH)
    # f.close()
    # user = Global.parseUser(userData)
    # return user

def getUserByName(userName):
    userName = str(userName).strip()
    #Number of users in file
    count = int(os.path.getsize(FILE_NAME)/USER_STRING_LENGTH)

    f = open(FILE_NAME, 'r')

    userData = ''
    i = 0
    for i in range(count):
        f.seek(i*USER_STRING_LENGTH + Global.USER_NAME_INDEX)
        if f.read(Global.USER_NAME_LENGTH).strip() == userName:
            f.seek(i*USER_STRING_LENGTH)
            userData = f.read(USER_STRING_LENGTH)
    f.close()
    user = Global.parseUser(userData)
    return user

def getUserByPhone(userPhone):
    userPhone = str(userPhone).strip()
    #Number of users in file
    count = int(os.path.getsize(FILE_NAME)/USER_STRING_LENGTH)

    f = open(FILE_NAME, 'r')

    userData = ''
    i = 0
    for i in range(count):
        f.seek(i*USER_STRING_LENGTH + Global.USER_PHONE_INDEX)
        if f.read(Global.USER_PHONE_LENGTH).strip() == userPhone:
            f.seek(i*USER_STRING_LENGTH)
            userData = f.read(USER_STRING_LENGTH)
    f.close()
    user = Global.parseUser(userData)
    return user

def getUserByEmail(userPhone):
    userPhone = str(userPhone).strip()
    #Number of users in file
    count = getNumberOfUsers()

    f = open(FILE_NAME, 'r')

    userData = ''
    i = 0
    for i in range(count):
        f.seek(i*USER_STRING_LENGTH + Global.USER_EMAIL_INDEX)
        if f.read(Global.USER_EMAIL_LENGTH).strip() == userPhone:
            f.seek(i*USER_STRING_LENGTH)
            userData = f.read(USER_STRING_LENGTH)
    f.close()
    user = Global.parseUser(userData)
    return user

def getNextId():
    #Number of users
    count = os.path.getsize(FILE_NAME)/USER_STRING_LENGTH
    return int(count+1)

def modifyUserData(user):
    index = (int(user.ID) - 1)*USER_STRING_LENGTH
    f = open(FILE_NAME, 'r+')
    f.seek(index)
    f.write(user.toString())
    f.close()

def deleteUser(user = User()):
    index = (int(user.ID) - 1) * USER_STRING_LENGTH
    f = open(FILE_NAME, 'r+')
    f.seek(index)
    f.write(' '*USER_STRING_LENGTH)
    f.close()
