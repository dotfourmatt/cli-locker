from modules import generate, ep, ef
from time import sleep
import os, ast, json

class Locker():
    def __init__(self):
        self.masterPassword = 'test'
        self.__mainLoop()
    
    # This function will run all functions in the application
    def __mainLoop(self):
        authenticated = self.__verifyUser()
        if authenticated:
            self.__checkFile()
            while authenticated:
                self.__selectAction()

    # Authenticates the user
    def __verifyUser(self):
        print(">>> Enter Master Password")
        masterInput = input(">>> ")
        attemps = 1
        if masterInput != self.masterPassword:
            while masterInput != self.masterPassword and attemps < 3:
                print(">>> Incorrect password enered!")
                masterInput = input(">>> ")
                attemps += 1
            
            print(">> Too many attempts!")
            return False

        else:
            print(">>> Success!")
            return True

    # Checks if locker file exists, this file will store all password data.
    def __checkFile(self):
        folderDirPath = f"{os.environ['APPDATA']}\\cli-locker\\"
        fileName = "locker.json"
        fileDirPath = folderDirPath + fileName
        if not os.path.exists(folderDirPath):
            f = open(f"{fileDirPath}", "x+")
            f.write(json.dumps({}))
            f.close()
            return  print(f">>> {fileDirPath} has been created.")

        elif not os.path.exists(fileDirPath):
            f = open(f"{fileDirPath}", "x+")
            f.write(json.dumps({}))
            f.close()
            return  print(f">>> {fileDirPath} has been created.")

        else:
            return print(f">>> {fileDirPath} already exists.")

    # User choose what they want to do
    def __selectAction(self):
        print(">>> Please enter a value to select what you would like to do.")
        print("==> 1: View passwords\n==> 2: Add an entry into your locker\n==> 3: Generate a new password\n==> 4: Help\n==> 5: Quit application")

        actionInput = input(">>> ")
        Actions(actionInput)

# The "Actions" class contains all the actions the user can perform
class Actions():
    def __init__(self, actionValue = int):
        self.__exceptionHandler(actionValue)
        if int(actionValue) == 1:
            self.__viewPasswords()
        elif int(actionValue) == 2:
            self.__addEntry()
        elif int(actionValue) == 3:
            self.__createPassword()
        elif int(actionValue) == 4:
           self. __help()
        elif int(actionValue) == 5:
            self.__quit()
        else:
            pass
    
    def __viewPasswords(self):
        with open(f"{os.environ['APPDATA']}\\cli-locker\\locker.json", "r") as file:    
            for line in file:
                record = line

        locker = ast.literal_eval(record) # Returns dictionary

        for record in locker:
            print(record)

    def __addEntry(self):
        pass

    def __createPassword(self):
        sleep(0.5)
        print(">>> Please choose what options you like:")
        print("==> 1: Lower case letters")
        print("==> 2: Upper case letters")
        print("==> 3: Numbers")
        print("==> 4: Symbols")
        print(">>> Please note that options should be separated with a space (e.g. '1 3 4' => for lower case letters, numbers and symbols)")
        choose = input(">>> ")
        options = self.__optList(choose.split())
        print(">>> How long would you like the password? (Minimum is 8 and maximum is 50)")
        length = int(input(">>> "))
        password = generate(length, options)
        print(f"Your new password: {password}")

    def __optList(self, options = list):
        for val in options:
            if isinstance(int(val), int) == False:
                raise ValueError(">>> A non-integer was entered...")
        
        if len(options) == 4:
            return [True, True, True, True]

        elif len(options) > 4:
            raise IndexError(">>> Too many values enterd!")

        elif len(options) < 1:
            raise IndexError(">>> Not enough values enterd!")

        else:
            tempList = []
            for val in options:
                tempList.append(int(val))

            ls = [True, True, True, True]

            if 1 not in tempList:
                ls[0] = False
            elif 2 not in tempList:
                ls[1] = False
            elif 3 not in tempList:
                ls[2] = False
            else:
                ls[3] = False

            return ls

    def __help(self):
        pass

    def __quit(self):
        print(">>> Are you sure you want to quit? (y/n)? ")
        opt = input(">>> ")
        if opt in ['y', 'Y', 'Yes', 'YEs', 'YES', 'yES', 'yeS', 'yes']:
            exit()
    
    def __exceptionHandler(self, val):
        avalaibleActions = [1, 2, 3, 4, 5]
        try:
            if isinstance(int(val), int):
                if int(val) not in avalaibleActions:
                    raise NotImplementedError(">>> Sorry! This action does not exist!")

                elif int(val) == 3:
                    raise NotImplementedError(">>> Sorry, this action has not yet been inplemented!")
                        
            else:
                raise ValueError(">>> Please enter an integer!")
        
        except Exception as e:
            print(e)
            sleep(1)