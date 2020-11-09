import unittest
from src.Event import Event
from src.User import User

class EventTester(unittest.TestCase):
    def setUp(self):
        self.owner = User("root", "root")
        self.event = Event(self.owner)

    def testInitOwner1(self):
        assert self.owner == self.event.getOwner(), "Owner not properly set or got (get)"

    def testOwner1(self):
        newOwner = User("^.*&\"\'%2|", "password")
        self.event.setOwner(newOwner)
        assert newOwner == self.event.getOwner(), "Owner not properly set or got (get)"

    def testOwner2(self):
        newOwner = User("askjfsa", "rohsdaifjas")
        self.event.setOwner(newOwner)
        assert self.event.getOwner() == newOwner, "getter or setter not working"

    def testOwner3(self):
        newOwner = User("askjfsa", "rohsdaifjas")

        self.event.setOwner(newOwner)
        firstCorrect = self.event.getOwner() == newOwner

        self.event.setOwner(newOwner)
        secondCorrect = self.event.getOwner() == newOwner

        assert firstCorrect and secondCorrect, "getter or setter not working"

    def testStart1(self):
        assert self.event.getStart() != None, "getStart is not intitally set to an number"

    def testStart2(self):
        value = 50183
        self.event.setStart(value)
        assert value == self.event.getStart(), "Event's setStart() and/or getStart() method is not working."

    def testStart3(self):
        value = 199210.021412
        self.event.setStart(value)
        assert value == self.event.getStart(), "Event's setStart() and/or getStart() method is not working."

    def testStart4(self):
        value = 0
        self.event.setStart(value)
        assert value == self.event.getStart(), "Event's setStart() and/or getStart() method is not working."

    def testEnd1(self):
        assert self.event.getEnd() != None, "getEnd is not intitally set to an number"

    def testEnd2(self):
        value = 50183
        self.event.setEnd(value)
        assert value == self.event.getEnd(), "Event's setEnd() and/or getEnd() method is not working."

    def testEnd3(self):
        value = 199210.021412
        self.event.setEnd(value)
        assert value == self.event.getEnd(), "Event's setEnd() and/or getEnd() method is not working."

    def testEnd4(self):
        value = 0
        self.event.setEnd(value)
        assert value == self.event.getEnd(), "Event's setEnd() and/or getEnd() method is not working."

    def testTitle1(self):
        value = "fasfsd.*"
        self.event.setTitle(value)
        assert value == self.event.getTitle(), "Event's setTitle() and/or getTitle() method is not working"

    def testAllDay1(self):
        value = True
        self.event.setAllDay(value)
        assert value == self.event.getAllDay(), "Event's setAllDay() and/or getAllDay() method is not accepting True as a parameter value"

    def testAllDay2(self):
        value = False
        self.event.setAllDay(value)
        assert value == self.event.getAllDay(), "Event's setAllDay() and/or getAllDay() method is not accepting False as a parameter value"

    def testInitGuests1(self):
        assert len(self.event.getGuests()) == 0 and type(self.event.getGuests()) == type([]), "Event's 'guest' field is not initally a list of size 0"

    def testInviteGuest1(self):
        guest = User("hisadf", "dsafios")
        self.event.invite(guest)
        assert guest in self.event.getGuests() , "Event's invite() and/or getGuests() method is not working"
