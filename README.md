# Benjamin Alpert's CS205A Individual Project

## UML Class Diagram

![UML Class Diagram](/docs/UML/UML.png)

## Failed Implementation

![Failed Implementation Screenshot](/docs/UML/FailedTestScreenshot.png)

### Correct Implementation
```python
  def findUser(self, name):
      for user in self.users:
          if(user.getName() == name):
              return user
      return None
```

### Incorrect Implementation
```python
  def findUser(self, name):
      for user in self.users:
          if(user == name):
              return user
      return None
```


## Description of Test Functions

Class Name | Function Name | Description
---------- | ------------- | -----------
CalendarTester | testInitUsers1 | Tests the 'users' field is a List object of size 1 when the object is initialized
CalendarTester | testInitUsers2 | Tests that the 'users' List's first element is a user with name 'root' (initially)
CalendarTester | testInitEvents1 | Tests to check that the 'events' fields is initially a List object of 0 elements
CalendarTester | testAddFindUsers1 |
CalendarTester | testAddFindUsers2
CalendarTester | testAddRemoveGetUsers1
CalendarTester | testAddFindUsers3
CalendarTester | testDoesUserExist1
CalendarTester | testAddEvent1
CalendarTester | testAddEvent2
CalendarTester | testRemoveEvent1
CalendarTester | testRemoveEvent2
CalendarTester | testDoesEventExist1
UserTester | testInitAuthorized1
UserTester | testInitAuthorized2
UserTester | testInitAuthorized3
UserTester | testInitName1
UserTester | testSetGetName
UserTester | testAuthorizeAndIsAuthorized1
UserTester | testUnauthorize
EventTester | testInitOwner1
EventTester | testOwner1
EventTester | testOwner2
EventTester | testInitOwner3
EventTester | testStart1
EventTester | testStart2
EventTester | testStart3
EventTester | testStart4
