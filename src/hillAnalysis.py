import random

import math

import sympy

import numpy as np

from math import gcd

from PIL import Image

from skimage import io

import matplotlib.pyplot as plt

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
    
def hillAnalysisSizeKnow(plain_text,encrypted_text,m):
    count = 0
    matrix_plain_text = []
    matrix_encrypted_text = []
    for i in range(int(len(plain_text) / m)):
        matrix_plain_text.append([])
        matrix_encrypted_text.append([])
        for j in range(m):
            matrix_plain_text[i].append(letters.find(plain_text[count]))
            matrix_encrypted_text[i].append(letters.find(encrypted_text[count]))
            count += 1
    #A = BK -> K = AB^(-1)
    A = sympy.Matrix(matrix_encrypted_text[0:m])
    B = sympy.Matrix(matrix_plain_text[0:m])
    B = B.inv_mod(26)
    K = (B*A)%26
    return K

print(hillAnalysisSizeKnow('FRIDAY','PQCFKU',2))