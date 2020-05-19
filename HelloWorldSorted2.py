import os.path

# Name of file to open 
filename = input('Enter a filename: ')

# Open file if it exists
if os.path.exists(filename):
    with open(filename) as f:
        nameList = f.readlines()
# If a file doesn't exist, let's create an empty list
else: 
    nameList = []

# Ask use for a name and add it to our list
print('When you are ready to exit, enter an empty name')
while True:
    name = input('Enter name: ')
    if name == '':
        break
    nameList.append(name + '\n')
    print('Hello, ' + name)

#Sort list alphabetically
nameList.sort()

#'w' will overwrite existing file
with open(filename, 'w', encoding='utf-8') as f: 
    f.writelines(nameList)