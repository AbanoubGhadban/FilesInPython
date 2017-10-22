from User import User

FILE_NAME = "users.txt"
USER_STRING_LENGTH = 100
USER_ID_LENGTH = 10
USER_NAME_LENGTH = 60
USER_PHONE_LENGTH = 30

USER_ID_INDEX = 0
USER_NAME_INDEX = USER_ID_LENGTH
USER_PHONE_INDEX = USER_NAME_INDEX + USER_NAME_LENGTH

def getUser(text):
    text = str(text)
    if len(text.strip("\n")) == 100 and len(text.strip()) > 0:
        user = User()
        user.ID = int(text[:10].strip())
        user.Name = text[10:70].strip()
        user.Phone = text[70:100].strip()
        return user

    return None