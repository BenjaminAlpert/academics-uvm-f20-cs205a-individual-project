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
  Ran 28 tests in 0.004s

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

  pyreverse -my -o png . --ignore=src.extras,tests
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
          if(user.getName() == name):
              return user
      return None
```

### Incorrect Implementation
```python
  def findUser(self, name):
      for user in self.users:
          if(user == name): #this link is incorrect
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
CalendarTester | testAddFindUsers2 |
CalendarTester | testAddRemoveGetUsers1 |
CalendarTester | testAddFindUsers3 |
CalendarTester | testDoesUserExist1 |
CalendarTester | testAddEvent1 |
CalendarTester | testAddEvent2 |
CalendarTester | testRemoveEvent1 |
CalendarTester | testRemoveEvent2 |
CalendarTester | testDoesEventExist1 |
UserTester | testInitAuthorized1 |
UserTester | testInitAuthorized2 |
UserTester | testInitAuthorized3 |
UserTester | testInitName1 |
UserTester | testSetGetName |
UserTester | testAuthorizeAndIsAuthorized1 |
UserTester | testUnauthorize |
EventTester | testInitOwner1 |
EventTester | testOwner1 |
EventTester | testOwner2 |
EventTester | testInitOwner3 |
EventTester | testStart1 |
EventTester | testStart2 |
EventTester | testStart3 |
EventTester | testStart4 |
