import passwordGenerator
import encryption
import saving
import pandas as pd

user = input('Insira o seu usuário: ')
game = input('Insira a applicação: ')

password = passwordGenerator.generatePassword()

encryptedPassword,key = encryption.encryptPassword(password)

encryptedPasswords = pd.DataFrame({'username': [user],'encrypted': [encryptedPassword], 'application': [game]})
keys = pd.DataFrame({'key': [key]})

saving.saveCsv(encryptedPasswords, 'encryptedPasswords.csv')
saving.saveCsv(keys, 'keys.csv')

applicationRequest = input('Insira a applicação: ')

indices, userNames, encryptedPasswords = saving.getData(applicationRequest)

index = saving.selectAccount(applicationRequest,indices, userNames)

key = saving.getKey(indices[index])

decryptedPassword = encryption.decryption(encryptedPasswords[index],key)

print('A senha é: {}'.format(decryptedPassword.decode('utf-8')))