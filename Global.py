from User import User

FILE_NAME = "users.txt"
USER_ID_LENGTH = 10
USER_NAME_LENGTH = 60
USER_PHONE_LENGTH = 30
USER_EMAIL_LENGTH = 30
USER_STRING_LENGTH = USER_ID_LENGTH + USER_NAME_LENGTH + USER_PHONE_LENGTH + USER_EMAIL_LENGTH

USER_ID_INDEX = 0
USER_NAME_INDEX = USER_ID_LENGTH
USER_PHONE_INDEX = USER_NAME_INDEX + USER_NAME_LENGTH
USER_EMAIL_INDEX = USER_PHONE_INDEX + USER_PHONE_LENGTH

#Convert string that we get from text file to User object
def parseUser(text):
    text = str(text)
    if len(text.strip("\n")) == USER_STRING_LENGTH and len(text.strip()) > 0:
        user = User()
        user.ID = int(text[:USER_ID_LENGTH].strip())

        #Index of last character of name + 1
        endOfNameIndex = USER_NAME_INDEX + USER_NAME_LENGTH
        user.Name = text[USER_ID_LENGTH:endOfNameIndex].strip()

        # Index of last character of phone + 1
        endOfPhoneIndex = USER_PHONE_INDEX + USER_PHONE_LENGTH
        user.Phone = text[USER_PHONE_INDEX:endOfPhoneIndex].strip()

        # Index of last character of email + 1
        endOfEmailIndex = USER_EMAIL_INDEX + USER_EMAIL_LENGTH
        user.Email = text[USER_EMAIL_INDEX:endOfEmailIndex].strip()
        return user

    return None