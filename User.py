

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.authorized = False

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        return 0

    def isAuthorized(self):
        return self.authorized

    def authorize(self, password):
        self.authorized = (self.password == password)
        return 0

    def unauthorize(self):
        self.authorized = False
        return 0
