import numpy as np

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequencyTable(plain_text):
    frequencyVec = np.zeros(26) 
    table = {}
    for i in range(len(plain_text)):
        position = letters.find(plain_text[i])
        frequencyVec[position] += 1
    frequencyVec = frequencyVec * 1/26
    for i in range(len(frequencyVec)):
        table[letters[i]] = frequencyVec[i]*100
    return table