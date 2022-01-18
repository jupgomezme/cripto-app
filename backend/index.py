from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from typing import Optional
from pydantic import BaseModel

import subprocess

from displacement import cesarEncryptionWithKey, cesarDecryptionWithKey, cesarEncryptionNoKey, cesarDecryptionNoKey
from hillImage import finalHillImage
from substitution import sustitutionEncryptionWithKey, sustitutionEncryptionNoKey, sustitutionDecryptionWithKey
from affine import affineEncryptionWithKey, affineEncryptionNoKey, affineDecryptionWithKey
from vigenere import vigenereEncryptionWithKey, vigenereEncryptionWithNoKey, vigenereDecryptionWithKey
from hill import hillEncryptionWithKey, hillEncryptionNoKey, hillDecryptionWithKey

from displacementAnalysis import breakCesarEncryption
from vigenereAnalysis import breakVigenereEncryption
from hillAnalysis import hillAnalysisSizeKnow

from file_helper import save_file, get_file_name_extended, data_path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    algorithm: Optional[str] = None
    action: Optional[str] = None
    data: Optional[str] = None
    key: Optional[str] = None
    encrypted_for_hill_analysis: Optional[str] = None
    matrix_size_for_hill_analysis: Optional[str] = None


@app.post("/")
def read_root(item: Item):
    algorithm = item.algorithm
    action = item.action
    data = item.data
    key = item.key
    encrypted_for_hill_analysis = item.encrypted_for_hill_analysis
    matrix_size_for_hill_analysis = item.matrix_size_for_hill_analysis

    data_processed = {}
    if algorithm == "displacement":
        if key or str(key) == "0":
            if action == "cipher":
                data_processed = cesarEncryptionWithKey(data, int(key))
            elif action == "decipher":
                data_processed = cesarDecryptionWithKey(data, int(key))
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
        if key:
            key = [int(element) for element in key.split(",")]
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

    elif algorithm == "hillAnalysis":
        data_processed = hillAnalysisSizeKnow(data, encrypted_for_hill_analysis, int(matrix_size_for_hill_analysis))

    else:
        return {
            "message": "wrong algorithm!"
        }

    return data_processed


@app.get("/update")
def update():
    with open('./../ci_cd.sh', 'rb') as file:
        script = file.read()
    rc = subprocess.call(script, shell=True)
    return rc


@app.post("/img", response_class=FileResponse)
async def create_file(
        file: UploadFile = File(...),
        action: str = Form(...)
):
    file_name = file.filename
    save_file(file)
    finalHillImage(file_name)

    if action == "cipher":
        output_file_name = get_file_name_extended(file_name)
    elif action == "decipher":
        output_file_name = get_file_name_extended(file_name, extended_part="-decoded")
    else:
        raise Exception("Wrong action!")

    return data_path + output_file_name
