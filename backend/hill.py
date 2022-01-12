import random

import math

import sympy

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def returnMatrixFromKey(key):
    if math.sqrt(len(key)) == int(math.sqrt(len(key))):
        matrix_key = []
        count = 0
        for i in range(int(math.sqrt(len(key)))):
            matrix_key.append([])
            for j in range(int(math.sqrt(len(key)))):
                matrix_key[i].append(letters.find(key[count]))
                count += 1
        return matrix_key


def hillEncryptionWithKey(plain_text, key):
    encrypted_text = ''
    if math.sqrt(len(key)) == int(math.sqrt(len(key))):
        matrix_key = []
        count = 0
        for i in range(int(math.sqrt(len(key)))):
            matrix_key.append([])
            for j in range(int(math.sqrt(len(key)))):
                matrix_key[i].append(letters.find(key[count]))
                count += 1
        A = sympy.Matrix(matrix_key)
        try:
            A = A.inv_mod(26)
        except ValueError:
            return 'Invalid key'

        excess = len(key) - (len(plain_text) - (int(len(plain_text) / len(key)) * len(key)))
        if excess != 0:
            for k in range(len(key) - excess):
                plain_text += 'X'
        matrix_text = []
        for k in range(int(len(plain_text) / len(key))):
            matrix_text.append([])
            for i in range(int(math.sqrt(len(key)))):
                matrix_text[k].append([])
                for j in range(int(math.sqrt(len(key)))):
                    matrix_text[k][i].append(letters.find(plain_text[0]))
                    plain_text = plain_text[1:]
        encrypted_matrix = []
        for k in range(len(matrix_text)):
            encrypted_matrix.append((sympy.Matrix(matrix_text[k]) * A) % 26)
        for k in range(len(encrypted_matrix)):
            for i in range(int(math.sqrt(len(key)))):
                for j in range(int(math.sqrt(len(key)))):
                    new_position = encrypted_matrix[k].row(i)[j]
                    encrypted_text += letters[new_position]

        return encrypted_text, returnMatrixFromKey(key)

    else:
        return 'Invalid key'


def hillEncryptionNoKey(plain_text):
    encrypted_text = ''
    keys = ["GYBNQKURP", "AIRPLANES", "DIFFICULT", "TEST"]
    key = keys[random.randint(0, len(keys) - 1)]
    encrypted_text = ''
    if math.sqrt(len(key)) == int(math.sqrt(len(key))):
        matrix_key = []
        count = 0
        for i in range(int(math.sqrt(len(key)))):
            matrix_key.append([])
            for j in range(int(math.sqrt(len(key)))):
                matrix_key[i].append(letters.find(key[count]))
                count += 1
        A = sympy.Matrix(matrix_key)
        try:
            A = A.inv_mod(26)
        except ValueError:
            return 'Invalid key'

        excess = len(key) - (len(plain_text) - (int(len(plain_text) / len(key)) * len(key)))
        if excess != 0:
            for k in range(len(key) - excess):
                plain_text += 'X'
        matrix_text = []
        for k in range(int(len(plain_text) / len(key))):
            matrix_text.append([])
            for i in range(int(math.sqrt(len(key)))):
                matrix_text[k].append([])
                for j in range(int(math.sqrt(len(key)))):
                    matrix_text[k][i].append(letters.find(plain_text[0]))
                    plain_text = plain_text[1:]
        encrypted_matrix = []
        for k in range(len(matrix_text)):
            encrypted_matrix.append((sympy.Matrix(matrix_text[k]) * A) % 26)
        for k in range(len(encrypted_matrix)):
            for i in range(int(math.sqrt(len(key)))):
                for j in range(int(math.sqrt(len(key)))):
                    new_position = encrypted_matrix[k].row(i)[j]
                    encrypted_text += letters[new_position]

        return encrypted_text, returnMatrixFromKey(key)

    else:
        return 'Invalid key'


def hillDecryptionWithKey(plain_text, key):
    encrypted_text = ''
    if math.sqrt(len(key)) == int(math.sqrt(len(key))):
        matrix_key = []
        count = 0
        for i in range(int(math.sqrt(len(key)))):
            matrix_key.append([])
            for j in range(int(math.sqrt(len(key)))):
                matrix_key[i].append(letters.find(key[count]))
                count += 1
        A = sympy.Matrix(matrix_key)
        try:
            A = A.inv_mod(26)
        except ValueError:
            return 'Invalid key'

        excess = len(key) - (len(plain_text) - (int(len(plain_text) / len(key)) * len(key)))
        if excess != 0:
            for k in range(len(key) - excess):
                plain_text += 'X'
        matrix_text = []
        for k in range(int(len(plain_text) / len(key))):
            matrix_text.append([])
            for i in range(int(math.sqrt(len(key)))):
                matrix_text[k].append([])
                for j in range(int(math.sqrt(len(key)))):
                    matrix_text[k][i].append(letters.find(plain_text[0]))
                    plain_text = plain_text[1:]
        encrypted_matrix = []
        for k in range(len(matrix_text)):
            encrypted_matrix.append((sympy.Matrix(matrix_text[k]) * A.inv_mod(26)) % 26)
        for k in range(len(encrypted_matrix)):
            for i in range(int(math.sqrt(len(key)))):
                for j in range(int(math.sqrt(len(key)))):
                    new_position = encrypted_matrix[k].row(i)[j]
                    encrypted_text += letters[new_position]

        return encrypted_text, returnMatrixFromKey(key)

    else:
        return 'Invalid key'
