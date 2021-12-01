from collections import OrderedDict

import math

import numpy as np

from displacementAnalysis import *
from src.vigenere import vigenereEncryptionWithKey, vigenereEncryptionWithNoKey

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

print(vigenereEncryptionWithKey('EL CRIPTOANALISIS ES LA PARTE DE LA CRIPTOLOGIA QUE SE DEDICA AL ESTUDIO DE SISTEMAS CRIPTOGRAFICOS CON EL FIN DE ENCONTRAR DEBILIDADES EN LOS SISTEMAS Y ROMPER SU SEGURIDAD SIN EL CONOCIMIENTO DE INFORMACION SECRETA  EN EL LENGUAJE NO TECNICO  SE CONOCE ESTA PRACTICA COMO ROMPER O FORZAR EL CODIGO  AUNQUE ESTA EXPRESION TIENE UN SIGNIFICADO ESPECIFICO DENTRO DEL ARGOT TECNICO  A LAS PERSONAS QUE SE DEDICAN AL CRIPTOANALISIS SE LES LLAMA CRIPTOANALISTAS','CLAVE'))            
key = breakVigenereEncryption('GW CMMREOVRCWINMU PS GE RLROI FP LV GTTPOSNZGDE SFE NI FPDDGC LL ZWVFDDS FP SDWVPMVW ECIKXQRRVJKNON GQY EG JKY DZ IPNOIXTLR YIDTLDHCOEN IP WON WKDTZQCD Y MSOAEM WW DEBYTTDVH UTN ZP EZNJGKXIZRVZ DZ MPQOMQCNIJR UPCMIVL  EI IN WEIKWLJZ RQ EEXRKNO  NI EZNJGG PSOE RCAXXKNA XSOZ RJQRPR J JQCZVV GW CJHKRO  VYPBUZ IUEA ZBRCENMQY TDIPP UI WKRNDJKNAYS GDPZGKQIXS FPNOVQ OEG ETROO XGNNDGQ  L LVW RPRNSPLS LYG DE YIFTCVR CW CMMREOVRCWINMU DE GIU WLVQC NRDTVZAIENTSOEU')
print(vigenereEncryptionWithNoKey('GW CMMREOVRCWINMU PS GE RLROI FP LV GTTPOSNZGDE SFE NI FPDDGC LL ZWVFDDS FP SDWVPMVW ECIKXQRRVJKNON GQY EG JKY DZ IPNOIXTLR YIDTLDHCOEN IP WON WKDTZQCD Y MSOAEM WW DEBYTTDVH UTN ZP EZNJGKXIZRVZ DZ MPQOMQCNIJR UPCMIVL  EI IN WEIKWLJZ RQ EEXRKNO  NI EZNJGG PSOE RCAXXKNA XSOZ RJQRPR J JQCZVV GW CJHKRO  VYPBUZ IUEA ZBRCENMQY TDIPP UI WKRNDJKNAYS GDPZGKQIXS FPNOVQ OEG ETROO XGNNDGQ  L LVW RPRNSPLS LYG DE YIFTCVR CW CMMREOVRCWINMU DE GIU WLVQC NRDTVZAIENTSOEU',key))