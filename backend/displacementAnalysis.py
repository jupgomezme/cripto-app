from frequencyTable import frequencyTable, letters

from displacement import cesarDecryptionWithKey

import math

letterFrequencyEng = {'A': 8.17, 'B': 1.29, 'C': 2.78, 'D': 4.25, 'E': 12.7,
                      'F': 2.23, 'G': 2.82, 'H': 6.89, 'I': 6.97, 'J': 0.15,
                      'K': 0.77, 'L': 4.83, 'M': 2.41, 'N': 6.75, 'O': 7.51,
                      'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.86,
                      'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97,
                      'Z': 0.07}


def difference(plain_text):
    frequencyPlainText = frequencyTable(plain_text)
    sum = 0
    for i in range(len(letters)):
        sum += abs(frequencyPlainText[letters[i]] - letterFrequencyEng[letters[i]])
    return sum / len(letters)


def breakCesarEncryption(plain_text):
    lowestDifference = math.inf
    encryptionKey = 0
    for key in range(0, 26):
        currentPlainText = cesarDecryptionWithKey(plain_text, key)
        currentDifference = difference(currentPlainText[0])
        if currentDifference < lowestDifference:
            lowestDifference = currentDifference
            encryptionKey = key
    return cesarDecryptionWithKey(plain_text, encryptionKey)
