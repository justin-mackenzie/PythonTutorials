print('Welcome to my first Hello World Program')
print('When you are ready to exit, enter an empty name')

nameList = []

while True:
    name = input('Enter name: ')
    if name == '':
        break
    nameList.append(name)
    print('Hello, ' + name)

print()
print("All the names entered were: ")
for n in nameList:
    print(n)
