import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def inversePermutation(permutation):
    for i in range(len(permutation)):
        actual = permutation[i]
        while actual != i:
            new = permutation[actual]
            permutation[actual] = actual
            actual = new
        permutation[actual] = actual
    return permutation

def inv(perm):
    inverse = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse[p] = i
    return inverse

print(inv([3, 0, 2, 1]))

def permutationEncryptionWithKey(plain_text, key):
    encrypted_text = ''
    if len(plain_text)%len(key)!=0:
        for i in range(len(key)-(len(plain_text)%len(key))):
            plain_text+='X'
    for i in range(int(len(plain_text)/len(key))):
        for j in range(len(key)):
            new_position = key[j]
            encrypted_text += plain_text[new_position+(i*len(key))]
    return encrypted_text, key

print(permutationEncryptionWithKey('HOLAMUNDOX',[1,2,0,3]))

def permutationEncryptionNoKey(plain_text,size):
    encrypted_text = ''
    key = random.sample(range(size), size)
    encrypted_text = ''
    if len(plain_text)%len(key)!=0:
        for i in range(len(key)-(len(plain_text)%len(key))):
            plain_text+='X'
    for i in range(int(len(plain_text)/len(key))):
        for j in range(len(key)):
            new_position = key[j]
            encrypted_text += plain_text[new_position+(i*len(key))]
    return encrypted_text, key

print(permutationEncryptionNoKey('HOLAMUNDOX',4))

def permutationDecryptionWithKey(plain_text, key):
    decrypted_text = ''
    key = inv(key)
    if len(plain_text)%len(key)!=0:
        for i in range(len(key)-(len(plain_text)%len(key))):
            plain_text+='X'
    for i in range(int(len(plain_text)/len(key))):
        for j in range(len(key)):
            new_position = key[j]
            decrypted_text += plain_text[new_position+(i*len(key))]
    return decrypted_text, key

print(permutationDecryptionWithKey('OLHAUNMDXXOX',[1,2,0,3]))