# Import the library we install in step 1
import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

SALT = b'SOME_RANDOM_SALT' 

def Encrypter(filename, password):
    password = password.encode() 

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=SALT,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    print('Opening file: ' + filename)
    with open(filename, 'rb') as f:
        data = f.read()

    print('Encrypting...')
    encryptedData = fernet.encrypt(data)

    print('Saving encrypted: ' + filename + '.enc')
    with open(filename + '.enc', 'wb') as f:
        f.write(encryptedData)

    print("----")
    print("DONE")

def Decrypter(filename, password):
    password = password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=SALT,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)

    # Open file 
    print('Opening encrypted file: ' + filename)
    with open(filename, 'rb') as f:
        encryptedFileData = f.read()

    # Decrypt
    print('Decrypting file...')
    decryptedFileData = fernet.decrypt(encryptedFileData)

    # Let's remove the .enc that we added when encrypting
    decryptedFilename = filename.replace('.enc','')
    # Let's add dec prefix just in case the old unecrypted file 
    # is still there. 
    decryptedFilename = 'dec_' + decryptedFilename

    print('Saving decrypted file data: ' + decryptedFilename)
    with open(decryptedFilename, 'wb') as f:
        f.write(decryptedFileData)

    print("----")
    print("DONE")
