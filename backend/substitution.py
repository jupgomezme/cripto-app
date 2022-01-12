import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def sustitutionEncryptionWithKey(plain_text, key):
    encrypted_text = ''
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            encrypted_text += ' '
        else:
            new_position = key.find(plain_text[i])
            encrypted_text += letters[new_position]
    return encrypted_text, key


def sustitutionEncryptionNoKey(plain_text):
    encrypted_text = ''
    letters_aux = letters
    key = ''
    for j in range(len(letters_aux)):
        choice = random.choice(letters_aux)
        key += choice
        letters_aux = letters_aux.replace(choice, "")
    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            encrypted_text += ' '
        else:
            new_position = key.find(plain_text[i])
            encrypted_text += letters[new_position]
    return encrypted_text, key


def sustitutionDecryptionWithKey(plain_text, key):
    encrypted_text = plain_text
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        if plain_text[i] == ' ':
            decrypted_text += ' '
        else:
            new_position = letters.find(encrypted_text[i])
            decrypted_text += key[new_position]
    return decrypted_text, key
