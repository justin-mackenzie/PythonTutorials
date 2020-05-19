import os.path

filename = input('Enter a filename: ')

# Define a menu function that returns
def Menu():
    print()
    print('*** Hello World Sorted ***')
    print('(1) Add name')
    print('(q) Save and quit')
    print('(x) Quick without Saving')
    userInput = input(': ')
    return userInput

if os.path.exists(filename):
    with open(filename) as f:
        nameList = f.readlines()
else: 
    nameList = []

print('When you are ready to exit, enter an empty name')
while True:
    userInput = Menu()
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