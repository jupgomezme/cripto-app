import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenereEncryptionWithKey(plain_text, key):
    encrypted_text = ''
    count = 0
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            encrypted_text += ' '
        else:
            position = letters.find(plain_text[i])
            new_position = (position + letters.find(key[count])) % 26
            encrypted_text += letters[new_position]
            count = (count + 1) % len(key)
    return encrypted_text, key


def vigenereEncryptionWithNoKey(plain_text):
    encrypted_text = ''
    keys = ["PYTHON", "JUMBLE", "EASY", "DIFFICULT", "ANSWER", "XYLOPHONE", "ATTACK", "DEFEND"]
    key = keys[random.randint(0, len(keys) - 1)]
    count = 0
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            encrypted_text += ' '
        else:
            position = letters.find(plain_text[i])
            new_position = (position + letters.find(key[count])) % 26
            encrypted_text += letters[new_position]
            count = (count + 1) % len(key)
    return encrypted_text, key


def vigenereDecryptionWithKey(plain_text, key):
    encrypted_text = plain_text
    decrypted_text = ''
    count = 0
    for i in range(len(encrypted_text)):
        if plain_text[i] == ' ':
            decrypted_text += ' '
        else:
            position = letters.find(encrypted_text[i])
            new_position = (position - letters.find(key[count])) % 26
            decrypted_text += letters[new_position]
            count = (count + 1) % len(key)
    return decrypted_text, key
