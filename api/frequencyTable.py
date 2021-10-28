import numpy as np
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def printFrequencyTable(plain_text):
    frequencyTable = np.zeros(26) 
    for i in range(len(plain_text)):
        position = letters.find(plain_text[i])
        frequencyTable[position] += 1
    frequencyTable = frequencyTable * 1/26
    print('Letter   |   Frequency')
    for i in range(len(frequencyTable)):
        print('   '+letters[i]+'     |   '+str(frequencyTable[i]))
    return letters,frequencyTable