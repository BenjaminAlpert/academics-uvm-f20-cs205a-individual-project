from DisplayPeriod import DisplayPeriod

class Displayer:
    def __init__(self, calendar):
        self.period = DislayPeriod.YEAR
        self.calendar = calendar

    def setPeriod(self, period):
        self.period = period

    def getDisplayText(self):
        text = ""
        for event in self.calendar.getEvents():
            text += "Title: %s\nStart: %d\nEnd: %d, Owner: %s\n\n" % (event.getTitle(), event.getStart(), event.getEnd(), event.getOwner().getName())
        return text
