import collections
import time
import operator

#crow modules
import config

class Storage(object):
    def __init__(self, timeToLive=config.timeToLive):
        self.store = collections.OrderedDict()
        self.timeToLive = timeToLive

    def __setitem__(self, key, value):
        self.cleanse()
        try: #If exists key in store
            self.store[key]
        except KeyError: #case key don't exists
            pass
        else: #case key exists
            del self.store[key] #delete key
        finally: #after all (always execute)
            self.store[key] = (time.monotonic(), value) #set the new key

    def __getitem__(self, key):
        self.cleanse()
        if key in self.store: return self.store[key][1]
        else: raise KeyError

    def __iter__(self):
        return iter(self.store)

    def cleanse(self, seconds=config.timeToLive):
        minAge = time.monotonic() + seconds
        numOfExpiredItems = len(list(filter(lambda entry: entry[0] >= minAge, self.store.values())))
        for _ in range(numOfExpiredItems): self.store.popitem(last=False)

    def get(self, key, default_value=None):
        if key in self.store: return self.store[key]
        return default_value

    @property
    def items(self): #Unused
        self.cleanse()
        return zip(self.store.keys(), map(operator.itemgetter(0), self.store.values()), map(operator.itemgetter(1), self.store.values()))


    def getLast(self):
        #start iterating self.store.values()
        for i in self.store:
            lastkey = i #the first iteration (also the last object put in the dict) is saved in lastkey
            break       #and the for loop breaks
        return [lastkey, self.store[lastkey]]
        #example: ['t', (172627.625, 'e')]
        # 't' is the key
        # 172627.625 is the result of time.monotonic()
        # 'e' is the value

    def printLast(self):
        entry = self.getLast()
        print("{0}: {1} - timeSinceCreated: {2}".format(
            entry[0], #key
            entry[1][1], #value
            time.monotonic() - entry[1][0] #time in hash table
            )
        )