import unittest
from src.Calendar import Calendar
from src.User import User
from src.Event import Event

class CalendarTester(unittest.TestCase):
    def setUp(self):
        self.calendar = Calendar()

    def testInitUsers1(self):
        assert len(self.calendar.getUsers()) == 1  and type(self.calendar.getUsers()) == type([]), "Initial 'users' attribute is not a list of size 1"

    def testInitUsers2(self):
        assert self.calendar.getUsers()[0].getName() == "root", "Initial 'user' is not a user with name root"

    def testInitEvents1(self):
        assert len(self.calendar.getEvents()) == 0 and type(self.calendar.getEvents()) == type([]), "Initial 'events' attribute is not a list of size 0"

    def testAddFindUsers1(self):
        user1 = User("user1", "sadfsjaf")
        self.calendar.addUser(user1)
        assert self.calendar.findUser("user1") == user1, "findUser not working"

    def testAddFindUsers2(self):
        user1 = User("user1", "a")
        user2 = User("user2", "b")
        user3 = User("user3", "")
        self.calendar.addUser(user1)
        self.calendar.addUser(user2)
        self.calendar.addUser(user3)
        assert self.calendar.findUser("user1") == user1 and self.calendar.findUser("user2") == user2 and self.calendar.findUser("user3") == user3, "findUsers method not working to find multiple users"

    def testAddRemoveGetUsers1(self):
        user1 = User("user1", "a")
        user2 = User("user2", "b")
        user3 = User("user3", "")
        self.calendar.addUser(user1)
        self.calendar.addUser(user2)
        self.calendar.addUser(user3)

        self.calendar.removeUser(user2)
        assert not (user2 in self.calendar.getUsers()), "error removing a user between two other users in a list"

    def testAddFindUsers3(self):
        user1 = User("user1", "sadfsjaf")
        user2 = User("user2", "sdfsa9")
        self.calendar.addUser(user1)
        assert self.calendar.findUser("user1") == user1 and self.calendar.findUser("user2") == None, "findUser() not working properly"

    def testDoesUserExist1(self):
        user1 = User("user1", "hioshafsi")
        user2 = User("user2", "sfas")
        self.calendar.addUser(user1)
        assert self.calendar.doesUserExist(user1) == True and self.calendar.doesUserExist(user2) == False, "doesUserExist(user) not working properly"

    def testAddEvent1(self):
        user1 = User("user1", "hioshafsi")
        event1 = Event(user1)
        event2 = Event(self.calendar.getUsers()[0])
        self.calendar.addEvent(event1)
        assert (event1 in self.calendar.getEvents()) and not (event2 in self.calendar.getEvents()), "addEvent(event) or getEvents() not working properly"

    def testAddEvent2(self):
        user1 = User("user1", "asfas")
        event1 = Event(user1)
        self.calendar.addEvent(event1)
        assert (user1 in self.calendar.getUsers()), "addEvent(event) is not adding unknown owners to calendar.users List"

    def testRemoveEvent1(self):
        user1 = User("user1", "asdi97")
        user2 = User("user2", "asdfu8")
        event1 = Event(user1)
        event2 = Event(user2)
        self.calendar.addEvent(event1)
        self.calendar.addEvent(event2)
        self.calendar.removeEvent(event1)
        assert event2 in self.calendar.getEvents() and not (event1 in self.calendar.getEvents()), "removing event fails"

    def testRemoveEvent2(self):
        user1 = User("user1", "asdi97")
        user2 = User("user2", "asdfu8")
        event1 = Event(user1)
        event2 = Event(user2)
        event3 = Event(self.calendar.getUsers()[0])
        self.calendar.addEvent(event1)
        self.calendar.addEvent(event2)
        self.calendar.removeEvent(event2)
        self.calendar.addEvent(event3)
        assert event1 in self.calendar.getEvents() and not (event2 in self.calendar.getEvents()) and event3 in self.calendar.getEvents(), "adding event after removing an event fails"

    def testDoesEventExist1(self):
        user1 = User("user1", "asdi97")
        user2 = User("user2", "asdfu8")
        event1 = Event(user1)
        event2 = Event(user2)
        self.calendar.addEvent(event1)
        assert self.calendar.doesEventExist(event1) and not self.calendar.doesEventExist(event2), "doesEventExist(event) not working"
