from Crypto.Cipher import AES
from Crypto import Random


def encryptImageAES(image):
    key = Random.new().read(AES.block_size)
    iv = Random.new().read(AES.block_size)
    input_file = open(image, 'rb')
    input_data = input_file.read()
    input_file.close()

    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(input_data)

    enc_file = open("encrypted.enc", "wb")
    enc_file.write(enc_data)
    enc_file.close()
    return key, iv


def decryptImageAES(enc, key, iv):
    enc_file2 = open(enc, 'rb')
    enc_data2 = enc_file2.read()
    enc_file2.close()

    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    plain_data = cfb_decipher.decrypt(enc_data2)

    output_file = open("output.jpg", "wb")
    output_file.write(plain_data)
    output_file.close()
    return key, iv


a = encryptImageAES('lena.jpg')
b = decryptImageAES("encrypted.enc", a[0], a[1])
