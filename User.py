import Global


class User:
    def __init__(self, ID="", Name="", Phone=""):
        self.ID = ID
        self.Name = Name
        self.Phone = Phone

    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self, value):
        self.__id = value

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @property
    def Phone(self):
        return self.__phone

    @Phone.setter
    def Phone(self, value):
        self.__phone = value

    __email = ''
    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self, value):
        self.__email = value

    #Return string with speceific length
    #If length of string is smaller than required length string will be appended with tailChar to end
    @staticmethod
    def __tailString(text, length, tailChar=' '):
        text=str(text)
        if len(text) > length:
            return text[:length]
        else:
            return text + tailChar*(length-len(text))

    #This function will convert User object to string
    #such as when you want to print User object
    #print(user)
    def __repr__(self):
        return "ID: {0}, Name: {1}, Phone: {2}, Email: {3}".format(self.ID, self.Name, self.Phone, self.Email)

    def toString(self):
        return "{0}{1}{2}{3}".format(User.__tailString(self.ID, Global.USER_ID_LENGTH),
                                  User.__tailString(self.Name, Global.USER_NAME_LENGTH),
                                  User.__tailString(self.Phone, Global.USER_PHONE_LENGTH),
                                  User.__tailString(self.Email, Global.USER_EMAIL_LENGTH))

    def getLastAppropIndex(self, text, char, maxIndex):
        index = text.rfind(char)
        while index > maxIndex and index > 0:
            index = text.rfind(char, 0, index)

        if index < 0:
            return maxIndex
        return index

    def getPrintableUser(self):
        nameLines = []
        tempName = self.Name
        while 1:
            if len(tempName) > Global.DISPLAYED_NAME_LENGTH:
                index = self.getLastAppropIndex(tempName, ' ', Global.DISPLAYED_NAME_LENGTH - 1)
                nameLines.append(tempName[:index+1])
                tempName = tempName[index+1:]
            else:
                nameLines.append(tempName)
                break

        idIndent = '{0:' + str(Global.DISPLAYED_ID_LENGTH) + '}  '
        nameIndent = '{1:' + str(Global.DISPLAYED_NAME_LENGTH) + '}  '
        phoneIndent = '{2:' + str(Global.DISPLAYED_PHONE_LENGTH) + '}  '
        emailIndent = '{3:' + str(Global.DISPLAYED_EMAIL_LENGTH) + '}  '

        text = (idIndent + nameIndent + phoneIndent + emailIndent).format(self.ID, nameLines[0], self.Phone, self.Email)
        for name in nameLines[1:]:
            text += '\n' + ' '*(Global.DISPLAYED_ID_LENGTH+2) + name
        return text

