NAME = 'name' 
FUNC = 'func'

def encryptFunc():
    print('ENCRYPTING')

def decryptFunc():
    print('DECRYPTING')

menuItem1 = { 
    'name': '(1) encrypt',
    'func': encryptFunc 
}

menuItem2 = {
    'name': '(2) decrypt',
    'func': decryptFunc 
}

menuItem3 = {
    'name': '(x) Exit'
}

# Lists within lists
menuData = {
    '1': menuItem1,
    '2': menuItem2,
    'x': { 'name': 'Exit'}
}

for menuNameNum, menuItem in menuData.items():
    print(menuNameNum + ' - ' + menuItem['name'])