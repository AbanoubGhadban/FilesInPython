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
