from collections import OrderedDict

import math

import numpy as np

from displacementAnalysis import *

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculateDistance(plain_text):
    sequences = plain_text.split()
    distanceVec = []
    for s in list(OrderedDict.fromkeys(sequences)):
        count = sequences.count(s)
        if count > 1:
            index = sequences.index(s)
            lastIndex = len(sequences) - sequences[::-1].index(s) - 1
            distance = 0
            for i in range(index, lastIndex):
                distance += len(sequences[i])
            distanceVec.append(distance)
    return np.gcd.reduce(distanceVec)

def divideBlock(plain_text,mcd):
    strings = "".join(plain_text.split())
    blocks = [strings[i:i+mcd] for i in range(0, len(strings), mcd)]
    return blocks

def group(content,mcd):
    lines = content
    groups = [""] * mcd
    for line in lines:
        for i in range(len(line)):
            groups[i] += line[i]
    return groups

def breakVigenereEncryption(plain_text):
    mcd = calculateDistance(plain_text)
    blocks = divideBlock(plain_text,mcd)
    segments = group(blocks,mcd)
    key = ''
    for element in segments:    
        key += letters[breakCesarEncryption(element)]
    return key