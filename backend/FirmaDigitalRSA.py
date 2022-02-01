import math

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import os
from file_helper import create_directory_if_not_exists

# Get the current working directory


keys_path = os.path.dirname(os.path.realpath(__file__)) + "/keys/"
data_path = os.path.dirname(os.path.realpath(__file__)) + "/data/"
create_directory_if_not_exists(keys_path)
# path =path[0:51]

# Cifrado y descifrado: cifrado de clave pública, descifrado de clave privada

# Verificación de firma: firma de clave privada, verificación de clave pública


key_name = "key"
bites = 3072
key_format = 'PEM'
random_generator = Random.new().read


# # Generador de números pseudoaleatorios

# # ejemplo de generación de algoritmo rsa
# rsa = RSA.generate(bites, random_generator)
#
#
# private_pem = rsa.exportKey()
#
# with open(path + f'{key_name}-private.pem', 'wb') as f:
#     f.write(private_pem)
#
# public_pem = rsa.publickey().exportKey()
#
# with open(path + f'{key_name}-public.pem', 'wb') as f:
#     f.write(public_pem)
#
# private_pem = rsa.exportKey()
#
# with open(path + f'{key_name}-private.pem', 'wb') as f:
#     f.write(private_pem)
#
# public_pem = rsa.publickey().exportKey()
#
# with open(path + f'{key_name}-public.pem', 'wb') as f:
#     f.write(public_pem)


# Cifrado, descifrado y muestra de claves
def encryptRSA(message):
    with open(keys_path + f'{key_name}-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(str(key))
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        # bytes_ = bytes(message.encode("utf8"))
        bytes_ = message
        cipher_text = base64.b64encode(cipher.encrypt(bytes_))
    return cipher_text, rsakey


def decryptRSA(cipher_text):
    with open(keys_path + f'{key_name}-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    return text, rsakey


def showPublicKey(keys):
    return keys.publickey().export_key(key_format).decode()


def showPrivateKey(keys):
    return keys.export_key(key_format).decode()


def generateSignature(message, key):
    with open(keys_path + f'{key_name}-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # bytes_ = bytes(message.encode("utf8"))
        bytes_ = message
        digest.update(bytes_)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
    return signature.decode("ascii"), key


def verifySignature(message, signature):
    with open(keys_path + f'{key_name}-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # bytes_ = bytes(message.encode("utf8"))
        bytes_ = message
        digest.update(bytes_)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
    return signature.decode("ascii"), key, is_verify


def signDocument(file_name):
    with open(data_path + file_name, mode='rb') as file:
        message = file.read()[:math.floor(bites / 8) - 11]

    a = encryptRSA(message)
    return generateSignature(message, a[1])


def fullVerifySignature(file_name, signature):
    with open(data_path + file_name, mode='rb') as file:
        message = file.read()[:math.floor(bites / 8) - 11]
    signature = signature.encode("ascii")
    try:
        s, k, v = verifySignature(message, signature)
    except:
        with open(keys_path + f'{key_name}-public.pem') as f:
            k = f.read()
            s = signature
            v = False
    return s, k, v
