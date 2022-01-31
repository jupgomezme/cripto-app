import random
from Crypto.Util.number import *
import codecs
import Crypto
from Crypto import Random

def encryption(plain_text, key):
    # c = m^2 mod n
    plain_text = padding(plain_text)
    plain_text = plain_text ** 2 % n
    return plain_text,key

def padding(plaintext):
    binary_str = bin(plaintext)     # convert to a bit string
    output = binary_str + binary_str[-16:]      # pad the last 16 bits to the end
    return int(output, 2)       # convert back to integer

def decryption(a, p, q):
    n = p * q
    r, s = 0, 0
    # find sqrt
    # for p
    if p % 4 == 3:
        r = sqrt_p_3_mod_4(a, p)
    elif p % 8 == 5:
        r = sqrt_p_5_mod_8(a, p)
    # for q
    if q % 4 == 3:
        s = sqrt_p_3_mod_4(a, q)
    elif q % 8 == 5:
        s = sqrt_p_5_mod_8(a, q)

    try:
        gcd, c, d = egcd(p, q)
        x = (r * d * q + s * c * p) % n
        y = (r * d * q - s * c * p) % n
        lst = [x, n - x, y, n - y]
        plain_text = choose(lst)
        if plain_text != None:
            string = bin(plain_text)
        else:
            return 'Something bad ocurred'
        string = string[:-16]
        plain_text = int(string, 2)
    except ValueError:
        return 'Something bad ocurred'

    return plain_text,[p,q]


# decide which answer to choose
def choose(lst):
    try: 
        for i in lst:
            binary = bin(i)
    
            append = binary[-16:]   # take the last 16 bits
            binary = binary[:-16]   # remove the last 16 bits
    
            if append == binary[-16:]:
                return i
    except ValueError:
        return 'Something bad ocurred'
    return 

# Find SQROOT in Zp where p = 3 mod 4
def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r


# Find SQROOT in Zp where p = 5 mod 8
def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p - 1) // 4, p)
    r =0
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p

    return r

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = egcd(b % a, a)
        return gcd, x - (b // a) * y, y
  
bits=600


while True:
        p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if ((p % 4)==3): break

while True:
        q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
        if ((p % 4)==3): break

n = p*q
msg="helloworldmotherfuckers!jajaaj"
plain_text =  bytes_to_long(msg.encode('utf-8'))
    
ciphertext = encryption(plain_text, n)
print(ciphertext[0])

plaintext = decryption(ciphertext[0], p, q)
try:
    st=format(plaintext[0], 'x')
    print(bytes.fromhex(st).decode())
except ValueError:
    print('Something bad ocurred, try again')