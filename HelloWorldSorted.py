print('Welcome to my first Hello World Program')
print('When you are ready to exit, enter an empty name')

# Name of file to open 
filename ='names.txt'

# Open existing names.txt file--it needs to be there 
# or else there will be an error
with open(filename) as f:
    nameList = f.readlines()

# Ask use for a name and add it to our list
while True:
    name = input('Enter name: ')
    if name == '':
        break
    nameList.append(name + '\n')
    print('Hello, ' + name)

#Sort list alphabetically
nameList.sort()

#'w' will overwrite existing file
with open(filename, 'w') as f: 
    f.writelines(nameList)