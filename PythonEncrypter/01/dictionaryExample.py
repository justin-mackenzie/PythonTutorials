# Not a working encrypt function
# just for the purpose of example 
def encryptFunc():
    print("ENCRYPTING")

# Example of a dictionary with a string and a function
menuItem = { 
    "name": "(1) encrypt",
    "func": encryptFunc 
}

# How we can access the name prop of our dictionary
print(menuItem["name"])
userInput = input(": ")

if userInput == '1':
    # We can even run the func that's in our dictionary
    menuItem["func"]()

