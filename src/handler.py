import json
from math import e
import numpy as np
from displacement import cesarEncryptionWithKey, cesarDecryptionWithKey, cesarEncryptionNoKey, cesarDecryptionNoKey
from substitution import sustitutionEncryptionWithKey, sustitutionEncryptionNoKey, sustitutionDecryptionWithKey
from affine import affineEncryptionWithKey, affineEncryptionNoKey, affineDecryptionWithKey
from vigenere import vigenereEncryptionWithKey, vigenereEncryptionWithNoKey, vigenereDecryptionWithKey
from hill import hillEncryptionWithKey, hillEncryptionNoKey, hillDecryptionWithKey

from displacementAnalysis import breakCesarEncryption
from vigenereAnalysis import breakVigenereEncryption

base_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": True,
    "Access-Control-Allow-Methods": "OPTIONS,POST,PUT,GET,DELETE"
}


def handler(event, context):

    print("in here")

    body = json.loads(event["body"])

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

    else:
        raise Exception("Wrong algorithm!")

    return {
        "statusCode": 200,
        "headers": base_headers,
        "body": json.dumps({"data_processed": data_processed})
    }