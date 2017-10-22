import Global


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

    @staticmethod
    def __tailString(text, length, tailChar=' '):
        text=str(text)
        if len(text) > length:
            return text[:length]
        else:
            return text + tailChar*(length-len(text))

    def __repr__(self):
        return "ID: {0}, Name: {1}, Phone: {2}".format(self.ID, self.Name, self.Phone)

    def toString(self):
        return "{0}{1}{2}".format(User.__tailString(self.ID, Global.USER_ID_LENGTH),
                                  User.__tailString(self.Name, Global.USER_NAME_LENGTH),
                                  User.__tailString(self.Phone, Global.USER_PHONE_LENGTH))
