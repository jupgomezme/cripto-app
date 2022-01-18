import string
import random


def generate_random_string(S=8):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    return str(ran)


def generate_random_binary_string(S=8):
    list_ = "01"
    ran = ''.join(random.choices(list_, k=S))
    return str(ran)
