from cryptography.fernet import Fernet

def encryptPassword(password):
    key = Fernet.generate_key()
    cipherSuite = Fernet(key)
    cipherText = cipherSuite.encrypt(password.encode('utf-8'))
    key = key.decode('utf-8')
    cipherText = cipherText.decode('utf-8')
    return cipherText,key

def decryption(encryptedPassword,key):
    cipher_suite = Fernet(key)
    decryptedPassword = cipher_suite.decrypt(encryptedPassword.encode('utf-8'))
    return decryptedPassword