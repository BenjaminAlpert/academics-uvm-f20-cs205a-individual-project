from Prompt import *
from Calendar import Calendar

class Interface:
    def __init__(self):
        self.calendar = Calendar()
        self.currentUser = self.calendar.getUsers()[0]
        self.prompts = [
            AuthorizePrompt(self),
            CreateUserPrompt(self),
            ListUsersPrompt(self),
            ExitPrompt(self),
            CreateEventPrompt(self),
            ListEventsPrompt(self)
        ]

        while(True):
            index = 0
            for prompt in self.prompts:
                print("(%d) %s" % (index, prompt.getText()))
                index += 1

            userInput = input("Select Option by Number: ")
            index = 0
            for prompt in self.prompts:
                if(userInput == "exit"):
                    exit(0)
                if(userInput == str(index)):
                    if(self.currentUser.isAuthorized() or index == 0):
                        promptReturnCode = prompt.prompt()
                        while(promptReturnCode != 0):
                            print("ERROR! Try again! (return code %d)" % promptReturnCode)
                            promptReturnCode = prompt.prompt()
                        actionReturnCode = prompt.doAction()
                        print(prompt.getMessage(actionReturnCode))
                    else:
                        print("ALERT: Access Denied!")
                elif(index == len(self.prompts)):
                    print("EROROR: Invalid option.")
                index += 1

Interface()

#1604617200
#1604618000
