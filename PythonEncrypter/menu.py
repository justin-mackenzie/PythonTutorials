# It's bad to use string literals everywhere so we
# willd define some constants to use instead
NAME = 'name' 
FUNC = 'func'

class Menu:
    # Class constructor in python
    def __init__(self, title):
        # title of our menu
        self.title = title
        # Our dictionary of dictionaries
        self.menuData = {}
        # Total number of items in menu
        self.itemsInMenu = 0

    def addMenuItem(self, name, func):
        # Menu number is the length of our menuData 
        # dictionary plus one
        menuNumber = len(self.menuData) + 1
        self.menuData[str(menuNumber)] = { NAME: name, FUNC: func }

    def run(self):
        while True:
            print ()
            print ()
            print ("*** " + self.title + " ***")
            print ()
            for menuNum, menuItem in self.menuData.items():
                print(menuNum + ' - ' + menuItem[NAME])
            print("x - exit")
            print()
            userInput = input(": ")

            if userInput == 'x':
                break

            #Select the right item from our menu or "false"
            #if it's not there
            selected = self.menuData.get(userInput, False)

            # User selected item that wasn't in our list
            if not selected:
                input("INVALID INPUT -- press enter to continue")
            else:
                #Run the function that was selected
                selected[FUNC]()
                input("Complete -- press enter to continue")