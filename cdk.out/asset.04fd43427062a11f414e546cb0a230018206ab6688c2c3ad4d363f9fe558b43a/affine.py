import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def affineEncryptionWithKey(plain_text,key):
    encrypted_text = ''      
    for i in range(len(plain_text)):
        if plain_text[i]==' ':
            encrypted_text += ' '
        else:
            position = letters.find(plain_text[i])
            new_position = (key[0]*position + key[1]) % 26
            encrypted_text += letters[new_position]
    return encrypted_text,key

def affineEncryptionNoKey(plain_text):
    encrypted_text = ''
    key = [random.randint(1, 26),random.randint(1, 26)]      
    for i in range(len(plain_text)):
        if plain_text[i]==' ':
            encrypted_text += ' '
        else:
            position = letters.find(plain_text[i])
            new_position = (key[0]*position + key[1]) % 26
            encrypted_text += letters[new_position]
    return encrypted_text,key

def affineDecryptionWithKey(plain_text,key):
    encrypted_text = plain_text
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        if plain_text[i]==' ':
            decrypted_text += ' '
        else:
            position = letters.find(encrypted_text[i])
            new_position = (int(pow(key[0], -1, 26))*(position - key[1])) % 26
            decrypted_text += letters[new_position]
    return decrypted_text,key
