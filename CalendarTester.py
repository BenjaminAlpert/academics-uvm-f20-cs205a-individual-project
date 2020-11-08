import unittest
from Calendar import Calendar

class CalendarTester(unittest.TestCase):
    def setUp(self):
        self.calendar = Calendar()

    def testInitUsers1(self):
        assert len(self.calendar.getUsers()) == 1, "Initial 'users' attribute is not a list of size 1"

    def testInitUsers2(self):
        assert self.calendar.getUsers()[0].getName() == "root", "Initial 'user' is not a user with name root"

    def testInitEvents1(self):
        assert len(self.calendar.getEvents()) == 0, "Initial 'events' attribute is not a list of size 0"

    def testGetSetUsers1(self):
        user1 = User("user1", "a")
        user2 = User("user2", "b")
        user3 = User("user3", "")
        self.calendar.addUser(user1)
        self.calendar.addUser(user2)
        self.calendar.addUser(user3)
        assert

    def testUsers():
        print(users)
