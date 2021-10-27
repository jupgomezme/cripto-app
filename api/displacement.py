letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def cesarEncryption(plain_text, key):
    encrypted_text = ''
    for i in range(len(plain_text)):
        position = letters.find(plain_text[i])
        new_position = (position + key) % 26
        encrypted_text += letters[new_position]
    return encrypted_text


# print(cesarEncryption('HELLOWORLD',3))
def cesarDecryption(plain_text, key):
    encrypted_text = plain_text
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        position = letters.find(encrypted_text[i])
        new_position = (position - key) % 26
        decrypted_text += letters[new_position]
    return decrypted_text
# print(cesarDecryption('KHOORZRUOG',3))
