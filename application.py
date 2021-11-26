from flask import Flask, request
import json
from displacement import cesarDecryptionNoKey, cesarDecryptionWithKey, cesarEncryptionNoKey, cesarEncryptionWithKey
from frequencyTable import frequencyTable
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/', methods=["GET"])
def check_api():
    return {
        "message": "The api works!"
    }

@application.route('/', methods=['POST'])
def index():
    body = json.loads(request.data)
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
        "data_processed": data_processed
    }


# @app.route('/frequency_table', methods=['POST'])
# def frequency_table():
#     body = json.loads(request.data)
#     data = body["data"]
#     frequency_table_ = frequencyTable(data)
#     return {
#         "frequency_table": list(frequency_table_)
#     }


if __name__ == "__main__":
    application.debug = True
    application.run()

