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

    def testInitOwner3(self):
        newOwner = User("root", "")
        self.event.setOwner(newOwner)
        assert newOwner == self.event.getOwner(), "Not properly setting owner in constructor"

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
