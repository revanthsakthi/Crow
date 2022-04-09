import hashlib
import random
from sys import byteorder

def genID(seed:bytes=None) -> int:
    """
    Generate and return a new node ID.
    If seed provided, return it's ID.

    seed must be a bytes object
    """
    #detect if seed provided
    if seed == None:
        #seed = random.getrandbits(255
        #).to_bytes(
        #    32, #the 255 bytes of random.getrandbits encodes in 32 long bytes object
        #    byteorder
        #)
        
        seed = random.randbytes(32)
        #in theory, it's faster

    #hash the thing
    hasher = hashlib.sha1(seed)
    id = int.from_bytes(hasher.digest(), byteorder)

    #fix id lenght
    if len(str(id)) <= 48:
        last = random.randint(1,9)
        id = id + int(
            str(last) + str('000000000000000000000000000000000000000000000000')
        )
    
    return id