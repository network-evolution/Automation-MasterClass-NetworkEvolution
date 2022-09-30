import string
import random

def password_generator():
    password = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits + string.ascii_lowercase, k=8))
    return password
