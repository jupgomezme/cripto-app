import json
import numpy as np
from displacement import cesarEncryptionWithKey, cesarDecryptionWithKey, cesarEncryptionNoKey, cesarDecryptionNoKey


def handler(event, context):

    body = json.loads(event["body"])

    algorithm = body["algorithm"]
    action = body["action"]
    data = body["data"]
    key = body["key"]

    if algorithm == "cesar":
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

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Methods": "OPTIONS,POST,PUT,GET,DELETE"
        },
        "body": json.dumps({"data_processed": data_processed})
    }
