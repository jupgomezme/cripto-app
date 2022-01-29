import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

bit_size = 2048
key_format = 'PEM'
keys = RSA.generate(bit_size)

def RSAEncryption(plain_text):
    cipher_rsa = PKCS1_OAEP.new(keys.publickey())
    enc_data = cipher_rsa.encrypt(plain_text.encode())
    return enc_data,keys

def RSADecryption(plain_text):
    decipher_rsa = PKCS1_OAEP.new(keys)
    dec_data = decipher_rsa.decrypt(plain_text)
    return dec_data,keys

def showPublicKey(keys):
    return keys.publickey().export_key(key_format).decode()

def showPrivateKey(keys):
    return keys.export_key(key_format).decode()

#encryption/decryption
enc = RSAEncryption('Hola Mundo')
print(enc[0])
dec = RSADecryption(enc[0])
print(dec[0])
#showing the keys
print(showPublicKey(enc[1]))
print(showPrivateKey(enc[1]))
