from Crypto.Cipher import DES
from Crypto.Hash import SHA256
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from file_helper import data_path

salt_const = b"$ez*}-d3](%d%$#*!)$#%s45le$*fhucdivyanshu75456dgfdrrrrfgfs^"
pi = 100005


def encrypt3DESImage(path, key):
    # opening the image file

    with open(data_path + path, 'rb') as imagefile:
        image = imagefile.read()

    # padding
    while len(image) % 8 != 0:
        image += b" "

    # hashing original image in SHA256
    hash_of_original = SHA256.new(data=image)
    key_enc = PBKDF2(key, salt_const, 48, count=pi)

    # Encrypting using triple 3 key DES

    cipher1 = DES.new(key_enc[0:8], DES.MODE_CBC, key_enc[24:32])
    ciphertext1 = cipher1.encrypt(image)
    cipher2 = DES.new(key_enc[8:16], DES.MODE_CBC, key_enc[32:40])
    ciphertext2 = cipher2.decrypt(ciphertext1)
    cipher3 = DES.new(key_enc[16:24], DES.MODE_CBC, key_enc[40:48])
    ciphertext3 = cipher3.encrypt(ciphertext2)

    # Adding hash at end of encrypted bytes
    ciphertext3 += hash_of_original.digest()

    # Saving the file encrypted
    dpath = data_path + "encoded_" + path
    with open(dpath, 'wb') as image_file:
        image_file.write(ciphertext3)
    return key


def decrypt3DESImage(image_path, key):
    encrypted_image_path = "encoded_" + image_path
    with open(data_path + encrypted_image_path, 'rb') as encrypted_file:
        encrypted_data_with_hash = encrypted_file.read()

    key_dec = key

    # extracting hash and cipher data without hash
    extracted_hash = encrypted_data_with_hash[-32:]
    encrypted_data = encrypted_data_with_hash[:-32]

    # salting and hashing password
    key_dec = PBKDF2(key_dec, salt_const, 48, count=pi)

    # decrypting using triple 3 key DES
    cipher1 = DES.new(key_dec[16:24], DES.MODE_CBC, key_dec[40:48])
    plaintext1 = cipher1.decrypt(encrypted_data)
    cipher2 = DES.new(key_dec[8:16], DES.MODE_CBC, key_dec[32:40])
    plaintext2 = cipher2.encrypt(plaintext1)
    cipher3 = DES.new(key_dec[0:8], DES.MODE_CBC, key_dec[24:32])
    plaintext3 = cipher3.decrypt(plaintext2)

    # hashing decrypted plain text
    hash_of_decrypted = SHA256.new(data=plaintext3)

    # saving the decrypted file
    epath = data_path + 'decoded_' + image_path
    with open(epath, 'wb') as image_file:
        image_file.write(plaintext3)
    return key


def finalTDESImage(file_name):
    encrypt3DESImage(file_name, 'aBcdefghfegrds54')
    decrypt3DESImage(file_name, 'aBcdefghfegrds54')
