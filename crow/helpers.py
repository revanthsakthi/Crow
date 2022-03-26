import hashlib
import random

def genID(seed=None):
    """
    Generate and return a new sha1 hash.
    If seed provided, return the sha1 hash of it
    """
    #detect if seed provided
    if seed == None:
        seed = random.getrandbits(255)

    #hash the thing
    hasher = hashlib.sha1()
    hasher.update(str(seed).encode())
    return hasher.hexdigest()
