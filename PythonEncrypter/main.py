from menu import Menu
from encrypter import Encrypter, Decrypter

def EncryptFunc():
    print()
    filename = input("Filename: ")
    password = input("Password: ")
    Encrypter(filename, password)

def DecryptFunc():
    print()
    filename = input("Filename: ")
    password = input("Password: ")
    Decrypter(filename, password)

mainMenu = Menu('Python Encrypter')
mainMenu.addMenuItem('Encrypt file', EncryptFunc)
mainMenu.addMenuItem('Decrypt file', DecryptFunc)
mainMenu.run()
