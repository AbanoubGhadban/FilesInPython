import os

from main import FILE_NAME


def getUserById(userId):
    userId = str(userId)
    userId = userId.strip()

    f = open(FILE_NAME, "r")

print(os.path.getsize(FILE_NAME))