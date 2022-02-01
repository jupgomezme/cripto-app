import random
from Crypto.Util.number import *
import codecs
import Crypto
from Crypto import Random

p = 2878539719255896840361180464307696692983744751911190511220425864847353346868813199833486851918997818468585162788028630754477269888288406164535563626894254657050269761937020776827467
q = 3180391538037816608000897400297382853964500986342780513131366274892814444829081064618268336943100773140987515011140074993065879579545398654957169359032328589002745631674712466489687
n = p * q


def rabinEncryption(plain_text, key=[p, q]):
    [p, q] = key
    plain_text = bytes_to_long(plain_text.encode('utf-8'))
    # c = m^2 mod n
    plain_text = padding(plain_text)
    plain_text = plain_text ** 2 % n
    return str(plain_text), [str(p), str(q)]


def padding(plaintext):
    binary_str = bin(plaintext)  # convert to a bit string
    output = binary_str + binary_str[-16:]  # pad the last 16 bits to the end
    return int(output, 2)  # convert back to integer


def rabinDecryption(a, key):
    [p, q] = key
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

    st = format(plain_text, 'x')
    plain_text = bytes.fromhex(st).decode()
    return str(plain_text), [str(p), str(q)]


# decide which answer to choose
def choose(lst):
    try:
        for i in lst:
            binary = bin(i)

            append = binary[-16:]  # take the last 16 bits
            binary = binary[:-16]  # remove the last 16 bits

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
    r = 0
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

# bits = 600
# while True:
#     p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#     if ((p % 4) == 3): break
#
# while True:
#     q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
#     if ((p % 4) == 3): break


# plain_text = "helloworldmotherfuckers!jajaaj"
#
#
# ciphertext = encryption(plain_text)
# print(ciphertext[0])
#
# plaintext = decryption(ciphertext[0], p, q)
# print(plaintext)

# plain_text = bytes_to_long(msg.encode('utf-8'))
# try:
# st = format(plaintext[0], 'x')
# print(bytes.fromhex(st).decode())
# except ValueError:
#     print('Something bad ocurred, try again')
#
