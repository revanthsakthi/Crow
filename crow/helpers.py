import hashlib
import random

def generateId(s=random.getrandbits(255)):
    return hashlib.sha1(s).digest()
