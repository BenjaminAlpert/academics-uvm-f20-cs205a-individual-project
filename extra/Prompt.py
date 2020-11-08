from src.User import User
from src.Event import Event
from extra.Displayer import Displayer
from extra.DisplayPeriod import DisplayPeriod
import unittest

class Prompt:
    text = "DEFAULT (DOES NOTHING)"

    def __init__(self, interface):
        self.interface = interface

    def prompt(self):
        return 0

    def getText(self):
        return self.text

    def getMessage(self, returnCode):
        if(returnCode == 0):
            return "SUCCESS"
        else:
            return "ERROR"

class ExitPrompt(Prompt):
    text = "Exit"
    def doAction(self):
        print("Bye")
        exit(0)


class CreateUserPrompt(Prompt):

    text = "Create New User (requires root)"

    def prompt(self):
        self.name = input("Enter name: ")
        self.password = input("Enter Password: ")
        return 0

    def doAction(self):
        if(self.interface.currentUser.getName() == "root"):
            self.user = User(self.name, self.password)
            returnCode = self.interface.calendar.addUser(self.user)
            if(returnCode == 0):
                return 0
            return 1
        return 2

    def getMessage(self, returnCode):
        if(returnCode == 0):
            return "Sucesffully Created New User"
        if(returnCode == 1):
            return "ALERT: Failed. Check if there is already a user named \"%s\"." % self.name
        if(returnCode == 2):
            return "ALERT: Access Denied. You must be root to add new user."

class AuthorizePrompt(Prompt):
    text = "Authorize"

    def prompt(self):
        self.name = input("Enter name: ")
        self.password = input("Enter password: ")
        return 0

    def doAction(self):
        for user in self.interface.calendar.getUsers():
            if(user.getName() == self.name):
                returnCode = user.authorize(self.password)
                if(returnCode == 0 and user.isAuthorized()):
                    self.interface.currentUser = user
                    return 0
                else:
                    return 1 # error

        return 2

    def getMessage(self, returnCode):
        if(returnCode == 0):
            return "Sucesffully logged in as \"%s\"" % self.name
        if(returnCode == 1):
            return "Authorization denied. Check you password."
        if(returnCode == 2):
            return "User not found."

class ListUsersPrompt(Prompt):
    text = "List Users"
    def doAction(self):
        print("User List:")
        for user in self.interface.calendar.getUsers():
            print(user.getName())
        return 0
    def getMessage(self, returnCode):
        if(returnCode == 0):
            return ""
        return "ERROR: Unknown Error"

class CreateEventPrompt(Prompt):
    text = "Create Event"

    def prompt(self):
        self.title = input("Enter Title: ")
        self.start = int(input("Enter Start Date (seconds since Epoch): ")) #TODO: integer checking
        self.end = int(input("Enter End Date (seconds since Epoch): ")) #TODO: integer checking
        return 0

    def doAction(self):
        self.event = Event(self.interface.currentUser)
        self.event.setTitle(self.title)
        self.event.setStart(self.start)
        self.event.setEnd(self.end)
        self.interface.calendar.addEvent(self.event)
        return 0

class ListEventsPrompt(Prompt):
    text = "List Events"

    def prompt(self):
        self.period = input("Enter Display Period (Day, Week, Month, Year): ").upper()
        return not (self.period == "DAY" or self.period == "WEEK" or self.period == "MONTH" or self.period == "YEAR")


    def doAction(self):
        displayPeriod = None
        if(self.period == "DAY"):
            displayPeriod = DisplayPeriod.DAY
        elif(self.period == "WEEK"):
            displayPeriod = DisplayPeriod.WEEK
        elif(self.period == "MONTH"):
            displayPeriod = DisplayPeriod.MONTH
        elif(self.period == "YEAR"):
            displayPeriod = DisplayPeriod.YEAR
        else:
            return 1

        self.displayer = Displayer(self.interface.calendar)
        self.displayer.setPeriod(displayPeriod)
        return 0

    def getMessage(self, returnCode):
        if(returnCode == 0):
            return self.displayer.getDisplayText()
        else:
            return "ERROR"

class DoTestsPrompt(Prompt):
    text = "Do Tests"

    def doAction(self):
        unittest.main()
