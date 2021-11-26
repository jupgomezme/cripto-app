import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cesarEncryptionWithKey(plain_text,key):
    encrypted_text = ''
    for i in range(len(plain_text)):
        if plain_text[i]==' ':
            encrypted_text += ' '
        else:
            position = letters.find(plain_text[i])
            new_position = (position + key) % 26
            encrypted_text += letters[new_position]
    return encrypted_text,key

def cesarEncryptionNoKey(plain_text):
    encrypted_text = ''
    key = random.randint(1, 26)
    for i in range(len(plain_text)):
        if plain_text[i]==' ':
            encrypted_text += ' '
        else: 
            position = letters.find(plain_text[i])
            new_position = (position + key) % 26
            encrypted_text += letters[new_position]
    return encrypted_text,key

def cesarDecryptionWithKey(plain_text,key):
    encrypted_text = plain_text
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        if plain_text[i]==' ':
            decrypted_text += ' '
        else:
            position = letters.find(encrypted_text[i])
            new_position = (position - key) % 26
            decrypted_text += letters[new_position]
    return decrypted_text,key

def cesarDecryptionNoKey(plain_text):
    encrypted_text = plain_text
    decrypted_array = []
    key_array = []
    for j in range(1,26):
        key = j
        key_array.append(key)
        decrypted_text = ''
        for i in range(len(encrypted_text)):
            if plain_text[i]==' ':
                decrypted_text += ' '
            else:
                position = letters.find(encrypted_text[i])
                new_position = (position - key) % 26
                decrypted_text += letters[new_position]
        decrypted_array.append(decrypted_text)
    return decrypted_array,key_array