import json
import numpy as np
from displacement import cesarEncryptionWithKey, cesarDecryptionWithKey, cesarEncryptionNoKey, cesarDecryptionNoKey
from substitution import sustitutionEncryptionWithKey, sustitutionEncryptionNoKey, sustitutionDecryptionWithKey
from affine import affineEncryptionWithKey, affineEncryptionNoKey, affineDecryptionWithKey

base_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": True,
    "Access-Control-Allow-Methods": "OPTIONS,POST,PUT,GET,DELETE"
}


def handler(event, context):

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

    if algorithm == "substitution":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = sustitutionEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = sustitutionDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = sustitutionEncryptionNoKey(data)

    if algorithm == "affine":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = affineEncryptionWithKey(data, key)
            elif action == "decipher":
                data_processed = affineDecryptionWithKey(data, key)
        else:
            if action == "cipher":
                data_processed = affineEncryptionNoKey(data)

    return {
        "statusCode": 200,
        "headers": base_headers,
        "body": json.dumps({"data_processed": data_processed})
    }
