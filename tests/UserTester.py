import unittest
from src.User import User

class UserTester(unittest.TestCase):
    def setUp(self):
        self.user1 = User("user1", "password1")
        self.user2 = User("user2", "password2")
        self.user3 = User("user3", "(.*)") #potential regex error/hack/confusion????

    def testInitAuthorized1(self):
        self.user1.authorize("(.*)")
        assert self.user1.isAuthorized() == False, "user1 authorized with invalid password"

    def testInitAuthorized2(self):
        assert self.user1.isAuthorized() == False, "user1 incorrectly initally authorized"

    def testInitAuthorized3(self):
        assert self.user3.isAuthorized() == False, "user3 incorrectly initally authorized"

    def testInitName1(self):
        assert self.user1.getName() == "user1" and self.user3.getName() == "user3", "getName() not working"

    def testSetGetName(self):
        self.user1.setName("user1-01.*")
        assert self.user1.getName() == "user1-01.*", "getName() not working properly"

    def testAuthorizeAndIsAuthorized1(self):
        self.user3.authorize("(.*)")
        assert self.user3.isAuthorized() == True, "user3 not authorized when password is entered correctly"

    def testUnauthorize(self):
        self.user2.authorize("password2")
        authorized1 = self.user2.isAuthorized()

        self.user2.unauthorize()
        authorized2 = self.user2.isAuthorized()

        assert authorized1 == True and authorized2 == False, "unauthorized() is not working"
