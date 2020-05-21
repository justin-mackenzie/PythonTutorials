import os.path
#import our custom module (menuModule.py)
import menuModule

filename = input('Enter a filename: ')

if os.path.exists(filename):
    with open(filename) as f:
        nameList = f.readlines()
else: 
    nameList = []

print('When you are ready to exit, enter an empty name')
while True:
    userInput = menuModule.Menu()
    #If return from function is 1
    if userInput == '1':
        name = input('Enter name: ')
        nameList.append(name + '\n')
        print(name + " added")
    #else if return from function is q
    elif userInput == 'q':
        save = True 
        break
    #else if return from function is x
    elif userInput == 'x':
        save = False
        break

# Only save if the user quit with 'q' not 'x'
if save:
    nameList.sort()
    with open(filename, 'w', encoding='utf-8') as f: 
        f.writelines(nameList)