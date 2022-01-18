from pyDes import des, CBC, PAD_PKCS5
import binascii


def DESEncrypt(s, key):
    """
         Cifrado DES
         : param s: cadena sin procesar
         : return: cadena encriptada, hexadecimal
    """
    secret_key = key
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en), key


def DESDecrypt(s, key):
    """
         Descifrado DES
         : param s: cadena encriptada, hexadecimal
         : return: cadena descifrada
    """
    secret_key = key
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de, key

# print(DESEncrypt('HOLAMUNDO', 'AASBFURE'))
# print(DESDecrypt('36b617f26eaee1773c65571a822b29c9', 'AASBFURE'))
