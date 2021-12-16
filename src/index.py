import json

# import sys
# import os
# sys.path.append("/mnt/efs/lib")

from displacement import cesarEncryptionWithKey, cesarDecryptionWithKey, cesarEncryptionNoKey, cesarDecryptionNoKey
from substitution import sustitutionEncryptionWithKey, sustitutionEncryptionNoKey, sustitutionDecryptionWithKey
from affine import affineEncryptionWithKey, affineEncryptionNoKey, affineDecryptionWithKey
from vigenere import vigenereEncryptionWithKey, vigenereEncryptionWithNoKey, vigenereDecryptionWithKey
from hill import hillEncryptionWithKey, hillEncryptionNoKey, hillDecryptionWithKey

from displacementAnalysis import breakCesarEncryption
from vigenereAnalysis import breakVigenereEncryption
from hillAnalysis import hillAnalysisSizeKnow

base_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": True,
    "Access-Control-Allow-Methods": "OPTIONS,POST,PUT,GET,DELETE"
}

# EFS_PATH = "/mnt/efs"
# REQUERIMENTS_FILE_PATH = EFS_PATH + "/requirements.txt"

# file_string = """
# cycler==0.11.0
# fonttools==4.28.3
# imageio==2.13.3
# kiwisolver==1.3.2
# matplotlib==3.5.1
# mpmath==1.2.1
# networkx==2.6.3
# numpy==1.21.4
# packaging==21.3
# Pillow==8.4.0
# pyparsing==3.0.6
# python-dateutil==2.8.2
# PyWavelets==1.2.0
# scikit-image==0.19.0
# scipy==1.7.3
# six==1.16.0
# sympy==1.9
# tifffile==2021.11.2
# """

def handler(event, context):
    
    body = json.loads(event["body"])
    # command = body["command"]
    # command_output = subprocess.getoutput(command)


    algorithm = body["algorithm"]
    action = body["action"]
    data = body["data"]
    key = body["key"]

    if algorithm == "displacement":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = cesarEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = cesarDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = cesarEncryptionNoKey(data)
            elif action == "decipher":
                data_processed = cesarDecryptionNoKey(data)

    elif algorithm == "substitution":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = sustitutionEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = sustitutionDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = sustitutionEncryptionNoKey(data)

    elif algorithm == "affine":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = affineEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = affineDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = affineEncryptionNoKey(data)

    elif algorithm == "vigenere":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = vigenereEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = vigenereDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = vigenereEncryptionWithNoKey(data)

    elif algorithm == "hill":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = hillEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = hillDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = hillEncryptionNoKey(data)

    elif algorithm == "displacementAnalysis":
        data_processed = breakCesarEncryption(data)

    elif algorithm == "vigenereAnalysis":
        data_processed = breakVigenereEncryption(data)

    # elif algorithm == "hillAnalysis":
    #     data_processed = hillAnalysisSizeKnow(plain_text,encrypted_text,m)

    else:
        raise Exception("Wrong algorithm!")

    return {
        "statusCode": 200,
        "headers": base_headers,
        "body": json.dumps({"data_processed": data_processed})
    }
