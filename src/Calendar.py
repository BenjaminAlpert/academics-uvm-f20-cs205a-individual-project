from src.User import User
from src.Event import Event

class Calendar:
    def __init__(self):
        self.events = []
        self.users = [User("root", "root")]

    def getEvents(self):
        return self.events

    def doesEventExist(self, event):
        return event in self.events


    def addEvent(self, event):
        if(not self.doesEventExist(event)):
            if(not event.getOwner() in self.users):
                self.addUser(event.getOwner())
            self.events.append(event)

    def removeEvent(self, event):
        if(self.doesEventExist(event)):
            self.events.remove(event)
            return 0
        return 1

    def getUsers(self):
        return self.users



    # Correct implementation of findUser
    def findUser(self, name):
        for user in self.users:
            if(user.getName() == name):
                return user
        return None

    """
    # Incorrect implementation of findUser:
    def findUser(self, name):
        for user in self.users:
            if(user == name):
                return user
        return None
    """



    def doesUserExist(self, user):
        return user in self.users

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
