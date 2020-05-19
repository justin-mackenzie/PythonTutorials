# Store input numbers
print('Welcome to my first Hello World Program')
print('When you are ready to exit, enter an empty name')

nameList = []
filename = 'names.txt'

while True:
    name = input('Enter name: ')
    if name == '':
        break

    with open(filename, 'a') as out:
        out.write(name+ '\n')

    print('Hello, ' + name)