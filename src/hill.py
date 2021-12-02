import random

import math

import sympy

import numpy as np

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def transposeMatrix(m):
    return np.array(m).T.tolist()

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def invmod(a,n):
    i=1
    while True:
        c = n * i + 1;
        if(c%a==0):
            c = c/a
            break;
        i = i+1
    return c
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    det = pow(determinant, -1, 26)
    if len(m) == 2:
        return [[m[1][1]*det, -1*m[0][1]*det],
                [-1*m[1][0]*det, m[0][0]*det]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]*det
    return cofactors

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

def hillEncryptionWithKey(plain_text,key):
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
        if A.det() == 0:
            return 'Invalid key'
        else:
            if len(plain_text) % int(math.sqrt(len(key))) != 0:
                for k in range(len(plain_text) % int(math.sqrt(len(key)))+1):
                    plain_text +='X'
            count_2 = 0
            matrix_text = []
            for i in range(int(len(plain_text) / math.sqrt(len(key)))):
                matrix_text.append([])
                for j in range(int(math.sqrt(len(key)))):
                    matrix_text[i].append(letters.find(plain_text[count_2]))
                    count_2 += 1
            B = sympy.Matrix(matrix_text)
            C = []
            for i in range(len(matrix_text)):
                C.append(A*B.row(i).T)
            for i in range(len(C)):
                for j in range(len(C[i].T.row(0))):
                    new_position = C[i].T.row(0)[j] % 26
                    encrypted_text += letters[new_position]
            return encrypted_text,returnMatrixFromKey(key)

    else:
        return 'Invalid key'


def hillEncryptionNoKey(plain_text):
    encrypted_text = ''
    keys = ["GYBNQKURP" , "AIRPLANES" , "EASY" , "DIFFICULT",  "XYLOPHONE" , "LOOK"]
    key = keys[random.randint(0, len(keys)-1)]
    if math.sqrt(len(key)) == int(math.sqrt(len(key))):
        matrix_key = []
        count = 0 
        for i in range(int(math.sqrt(len(key)))):
            matrix_key.append([])
            for j in range(int(math.sqrt(len(key)))):
                matrix_key[i].append(letters.find(key[count]))
                count += 1
        A = sympy.Matrix(matrix_key)
        if A.det() == 0:
            return 'Invalid key'
        else:
            if len(plain_text) % int(math.sqrt(len(key))) != 0:
                for k in range(len(plain_text) % int(math.sqrt(len(key)))+1):
                    plain_text +='X'
            count_2 = 0
            matrix_text = []
            for i in range(int(len(plain_text) / math.sqrt(len(key)))):
                matrix_text.append([])
                for j in range(int(math.sqrt(len(key)))):
                    matrix_text[i].append(letters.find(plain_text[count_2]))
                    count_2 += 1
            B = sympy.Matrix(matrix_text)
            C = []
            for i in range(len(matrix_text)):
                C.append(A*B.row(i).T)
            for i in range(len(C)):
                for j in range(len(C[i].T.row(0))):
                    new_position = C[i].T.row(0)[j] % 26
                    encrypted_text += letters[new_position]
            return encrypted_text,returnMatrixFromKey(key)

    else:
        return 'Invalid key'

def hillDecryptionWithKey(plain_text,key):
    encrypted_text = ''
    if math.sqrt(len(key)) == int(math.sqrt(len(key))):
        matrix_key = []
        count = 0 
        for i in range(int(math.sqrt(len(key)))):
            matrix_key.append([])
            for j in range(int(math.sqrt(len(key)))):
                matrix_key[i].append(letters.find(key[count]))
                count += 1
        A = sympy.Matrix(getMatrixInverse(matrix_key))
        if A.det() == 0:
            return 'Invalid key'
        else:
            if len(plain_text) % int(math.sqrt(len(key))) != 0:
                for k in range(len(plain_text) % int(math.sqrt(len(key)))+1):
                    plain_text +='X'
            count_2 = 0
            matrix_text = []
            for i in range(int(len(plain_text) / math.sqrt(len(key)))):
                matrix_text.append([])
                for j in range(int(math.sqrt(len(key)))):
                    matrix_text[i].append(letters.find(plain_text[count_2]))
                    count_2 += 1
            B = sympy.Matrix(matrix_text)
            C = []
            for i in range(len(matrix_text)):
                C.append(A*B.row(i).T)
            for i in range(len(C)):
                for j in range(len(C[i].T.row(0))):
                    new_position = C[i].T.row(0)[j] % 26
                    encrypted_text += letters[new_position]
            return encrypted_text,returnMatrixFromKey(key)

    else:
        return 'Invalid key'