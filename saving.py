import pandas as pd
from cryptography.fernet import Fernet
import os
import numpy as np

def saveCsv(df, filename):
    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        with open(filename, 'a') as file:
            existing_df = pd.read_csv(filename)
            file.write(df.iloc[:, :existing_df.shape[1]].to_csv(header=False, index=False))

def fomatting(text):
    return text.replace(" ", "").lower()

def getData(application):
    encryptedPasswords = pd.read_csv('encryptedPasswords.csv')
    application = fomatting(application)
    encryptedPasswords = encryptedPasswords[encryptedPasswords['application'] == application]
    indices = encryptedPasswords.index.tolist()
    userNames = encryptedPasswords['username'].tolist()
    encryptedPasswords = encryptedPasswords['encrypted'].tolist()
    return indices, userNames, encryptedPasswords

def getKey(indices):
    keys = pd.read_csv('keys.csv')
    keys = keys.iloc[indices,0]
    return keys

def selectAccount(application,indices, userNames):
    print('Existing accounts in {}: '.format(application))
    for i in range(len(indices)):
        print('{}. {}'.format(i, userNames[i]))
    index = int(input('Insira o número correspondente a conta desejada: '))
    return indices[index]