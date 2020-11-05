import time

class Event:
    def __init__(self, owner):
        self.owner = owner

        #defaults
        self.start = time.time()
        self.end = time.time() + (2*60*60) # plus 2 hours
        self.allDay = False
        self.title = "Unnamed Event"
        self.guests = []

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    def getAllDay(self):
        return self.allDay

    def setAllDay(self, allDay):
        self.allDay = allDay

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getOwner(self):
        return owner

    def setOwner(self, owner):
        self.owner = owner

    def invite(self, guest):
        self.guests.append(guest)

    def getGuests(self):
        return self.guests
