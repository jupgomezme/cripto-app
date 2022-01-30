import json
import random
from math import pow

a = random.randint(2, 10)


def list_to_string(list_):
    return [str(element) for element in list_]


def list_to_int(list_):
    return [int(element) for element in list_]


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)


# Generating large random numbers
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c


# Asymmetric encryption
def encrypt(msg, q, h, g):
    en_msg = []

    k = gen_key(q)  # Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p


def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg


q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)


def ElGamalEncryption(plain_text):
    key = gen_key(q)  # Private key for receiver
    h = power(g, key, q)
    en_msg, p = encrypt(plain_text, q, h, g)
    en_msg = list_to_string(en_msg)
    key, p = list_to_string([key, p])
    return en_msg, (key, p)


def ElGamalDecryption(plain_text, key_and_p):
    plain_text = list_to_int(plain_text)
    key, p = list_to_int(key_and_p)
    dr_msg = decrypt(plain_text, p, key, q)
    dmsg = ''.join(dr_msg)
    key, p = list_to_string([key, p])
    return dmsg, (key, p)

#
# a = ElGamalEncryption('HELLO WORLD')
# print(a[0])
# print(a[1])
# b = ElGamalDecryption(a[0], a[1])
# print(b)
