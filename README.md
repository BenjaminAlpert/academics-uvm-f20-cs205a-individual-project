# Benjamin Alpert's CS205A Individual Project

## Usage

### Starting
```bash
  git clone https://github.com/BenjaminAlpert/academics-uvm-f20-cs205a-individual-project.git
  python3 academics-uvm-f20-cs205a-individual-project

```

### Running
```
  Authorize with name 'root' and password 'root' to start


  (0) Authorize
  (1) Do Tests
  (2) Create New User (requires root)
  (3) List Users
  (4) Create Event
  (5) List Events
  (6) Exit

  Select Option by Number: 0
  Enter name: root
  Enter password: root
```
```
  Successfully logged in as "root"

  (0) Authorize
  (1) Do Tests
  (2) Create New User (requires root)
  (3) List Users
  (4) Create Event
  (5) List Events
  (6) Exit

  Select Option by Number: 1
  ............................
  ----------------------------------------------------------------------
  Ran 28 tests in 0.001s

  OK
```


## UML Class Diagrams

### UML Generation
I used [pylint's](https://pypi.org/project/pylint/) `pyreverse` command to generate the UML Class Diagrams.

First, I installed [pylint](https://pypi.org/project/pylint/):
```bash
  sudo apt install pylint
```

Alternatively, I could have installed [pylint](https://pypi.org/project/pylint/) with pip:
```bash
  pip install pylint
```

Then, I generated the UML Class Diagrams with the below commands
```bash
  cd academics-uvm-f20-cs205a-individual-project

  pyreverse -my -o png . --ignore=extras,tests
  mv classes.png ./docs/UML/entities.png

  pyreverse -my -o png . --ignore=src
  mv classes.png ./docs/UML/tests.png

  pyreverse  -my -o png src/extras
  mv classes.png ./docs/UML/extras.png

  pyreverse  -my -o png .
  mv classes.png ./docs/UML/full_package.png

  rm packages.png
```

### Entities
![Entities UML Diagram](/docs/UML/entities.png)

### Tests
![Tests UML Class Diagram](/docs/UML/tests.png)

### Extras
![Extras UML Class Diagram](/docs/UML/extras.png)

### Full Package
![Full UML Class Diagram](/docs/UML/full_package.png)







## Failed Test

![Failed Implementation Screenshot](/docs/failed_test_screenshot.png)

### Correct Implementation
```python
  def findUser(self, name):
      for user in self.users:
          if(user.getName() == name): #This line is correct: It compares a 'name' string to a 'name' string
              return user
      return None
```

### Incorrect Implementation
```python
  def findUser(self, name):
      for user in self.users:
          if(user == name): #this line is incorrect: It compares a 'name' string to a User object
              return user
      return None
```


## Description of Test Functions

Class Name | Function Name | Description
---------- | ------------- | -----------
CalendarTester | testInitUsers1 | Tests the 'users' field is a List object of size 1 when the object is initialized
CalendarTester | testInitUsers2 | Tests that the 'users' List's first element is a user with name 'root' (initially)
CalendarTester | testInitEvents1 | Tests to check that the 'events' fields is initially a List object of 0 elements
CalendarTester | testAddFindUsers1 | Tests to check that an uers object added can be found
CalendarTester | testAddFindUsers2 | Test if multiple users objects are added, can they all be found?
CalendarTester | testAddRemoveGetUsers1 | Tests for removing (multiple) users
CalendarTester | testAddRemoveGetUsers2 | Tests for removing a user in between two other users that are not removed
CalendarTester | testAddFindUsers3 | Tests for adding only one user
CalendarTester | testDoesUserExist1 | Tests Calendar.doesUserExist(self, user) method by adding a user and not adding another user
CalendarTester | testAddEvent1 | Tests addEvent(event) and getEvents() methods
CalendarTester | testAddEvent2 | Checks that unknown 'owner' user objects are added to the calendar object if not already added
CalendarTester | testRemoveEvent1 | Tests event removal
CalendarTester | testRemoveEvent2 | Tests event removal with non collated adding/removing order
CalendarTester | testDoesEventExist1 | Tests that this works properly by creating two events and adding one. Then, checking if passing in the added event object returns true while the passing in the nonadded event object returns false
UserTester | testInitAuthorized1 | Checks that the initially set password can be authorized with the same password string. Basically, ensures that the 'password' field is set properly
UserTester | testInitAuthorized2 | Tests to check that the user is initially unauthorized
UserTester | testInitName1 | Tests to check that the 'name' field is initially set correctly
UserTester | testSetGetName | Tests the getName() method
UserTester | testAuthorizeAndIsAuthorized1 | Tests to check that incorrect passwords are not able to authorize a user
UserTester | testUnauthorize | Tests that unauthorize() method works by using the isAuthorized() method
EventTester | testInitOwner1 | Tests that ownership is initially set to the passed in user object
EventTester | testOwner1 | Tests getter and/or setter of 'owner' field with some special characters ("^.*&\"\'%2|")
EventTester | testOwner2 |
EventTester | testInitOwner3 |
EventTester | testStart1 |
EventTester | testStart2 |
EventTester | testStart3 |
EventTester | testStart4 |
