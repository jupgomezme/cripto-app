from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import os

# Get the current working directory
path = os.path.realpath(__file__)
path =path[0:51]

# Cifrado y descifrado: cifrado de clave pública, descifrado de clave privada
#
 # Verificación de firma: firma de clave privada, verificación de clave pública
#
print ("1, generar clave privada y clave pública")
 
 # Generador de números pseudoaleatorios
random_generator = Random.new().read
 # ejemplo de generación de algoritmo rsa
rsa = RSA.generate(1024, random_generator)

key_format = 'PEM'

private_pem = rsa.exportKey()
 
with open(path+'aaa-private.pem', 'wb') as f:
    f.write(private_pem)
 
public_pem = rsa.publickey().exportKey()

with open(path+'aaa-public.pem', 'wb') as f:
    f.write(public_pem)
 
private_pem = rsa.exportKey()

with open(path+'bbb-private.pem', 'wb') as f:
    f.write(private_pem)
 
public_pem = rsa.publickey().exportKey()

with open(path+'bbb-public.pem', 'wb') as f:
    f.write(public_pem)
 
# Cifrado, descifrado y muestra de claves
def encryptRSA(message):
    with open('bbb-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(str(key))
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
    return cipher_text,rsakey

a = encryptRSA('Hola a todos, estos son los datos que quiero cifrar')
print(a[0])

def decryptRSA(cipher_text): 
    with open('bbb-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    return text,rsakey

b = decryptRSA(a[0])
print(b[0])

def showPublicKey(keys):
    return keys.publickey().export_key(key_format).decode()

def showPrivateKey(keys):
    return keys.export_key(key_format).decode()

print(showPrivateKey(b[1]))

def generateSignature(message,key):
    with open('aaa-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode("utf8"))
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
    return signature, key

c = generateSignature('Hola a todos, estos son los datos que quiero cifrar',a[1])
print(c[0])
 
def verifySignature(message,signature,key):
    with open('aaa-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode("utf8"))
        is_verify = verifier.verify(digest, base64.b64decode(signature))
    return is_verify,signature,key

d = verifySignature('Hola a todos, estos son los datos que quiero cifrar',c[0],c[1])
print(d[0])