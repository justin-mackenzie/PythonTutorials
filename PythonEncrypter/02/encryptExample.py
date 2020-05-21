# Import the library we install in step 1
import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Password we'll supply to the method eventually
password_provided = "password" 
# Turn password into a bit array
password = password_provided.encode() 

# Setup the KDF with a salt, which will be used to 
# create a key from the password
salt = b'SOME_RANDOM_SALT' 
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

# Create the key
key = base64.urlsafe_b64encode(kdf.derive(password))
# Start fernet (specific implementation of AES-128)
fernet = Fernet(key)

# *** Show Encrypting a File ***

# Open the file as a bit array
print('Opening file: FileToEncypt.txt')
with open('FileToEncrypt.txt', 'rb') as f:
    data = f.read()

# Encrypt data
print('Encrypting')
encryptedData = fernet.encrypt(data)

# Save to output
print('Saving encrypted: EncryptedFile.txt')
with open('EncryptedFile.txt', 'wb') as f:
    f.write(encryptedData)

# *** Show Decrypting a File ***

# Open file 
print('Opening encrypted file')
with open('EncryptedFile.txt', 'rb') as f:
    encryptedFileData = f.read()

# Decrypt
print('Decrypting file')
decryptedFileData = fernet.decrypt(encryptedFileData)

# Save decrypted file
print('Saving decrypted file data')
with open('DecryptedFile.txt', 'wb') as f:
    f.write(decryptedFileData)

print("----")
print("DONE")