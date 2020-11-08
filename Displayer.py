from DisplayPeriod import DisplayPeriod
import time

class Displayer:
    def __init__(self, calendar):
        self.period = DisplayPeriod.YEAR
        self.calendar = calendar

    def setPeriod(self, period):
        self.period = period
        self.duration = 0
        if(period is DisplayPeriod.YEAR):
            self.duration = 60*60*24*365
        elif(period is DisplayPeriod.MONTH):
            self.duration = 60*60*24*31
        elif(period is DisplayPeriod.WEEK):
            self.duration = 60*60*24*7
        elif(period is DisplayPeriod.DAY):
            self.duration = 60*60*24
        else:
            return 1

        return 0

    def getDisplayText(self):
        text = ""
        for event in self.calendar.getEvents():
            if(event.getStart() <= time.time() and event.getEnd() >= time.time() - self.duration):
                text += "Title: %s, Start: %d, End: %d, Owner: %s\n" % (event.getTitle(), event.getStart(), event.getEnd(), event.getOwner().getName())
        return text
