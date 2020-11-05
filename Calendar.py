from User import User
from Event import Event

class Calendar:
    def __init__(self):
        self.events = []
        self.users = [User("root", "root")]

    def getEvents(self):
        return self.events

    def doesEventExist(self, event):
        for e in self.events:
            if(e == event):
                return True
        return False


    def addEvent(self, event):
        if(not self.doesEventExist(event)):
            self.events.append(event)

    def removeEvent(self, event):
        self.events.remove(event)
        return -1

    def getUsers(self):
        return self.users

    def findUser(self, name):
        for user in self.users:
            if(user.getName() == name):
                return user
        return None

    def doesUserExist(self, user):
        for u in self.users:
            if(u.getName() == user.getName()):
                return True
        return False

    def addUser(self, user):
        if(not self.doesUserExist(user)):
            self.users.append(user)
            return 0
        return 1

    def removeUser(self, user):
        if(user.getName() == "root"):
            return 2
        if(self.doesUserExist(user)):
            self.users.remove(user)
            return 0
        return 1
