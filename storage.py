import collections
import time
import operator

import config

class Storage(object):
    """
        General storage interface
    """
    #Builtins Accessors
    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, key):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    #Special Accessors
    def get(self, key, default_value=None):
        raise NotImplementedError

class TempStore(Storage):
    def __init__(self, timeToLive=config.timeToLive):
        self.store = collections.OrderedDict()
        self.timeToLive = timeToLive

    def __setitem__(self, key, value):
        self.cleanse()
        if self.store[key]: del self.store(key) #for updates
        self.store[key] = (time.monotonic, value)

    def __getitem__(self, key):
        self.cleanse()
        if key in self.store: return self.store[key][1]

    def __iter__(self):
        return iter(self.store)

    def cleanse(self, seconds=config.timeToLive):
        minAge = time.monotonic() - seconds
        itemsToDelete = len(list(filter(lambda entry: entry[0] >= minAge, self.store.values())))
        for _ in range(itemsToDelete): self.store.popitem(last=False)

    def get(self, key, default_value=None):
        if key in self.store: return self.store[key]
        return default_value

    @property
    def items(self):
        self.cleanse()
        return zip(
            self.data.keys(),
            map(operator.itemgetter(0), self.data.values)
            map(operator.itemgetter(1), self.data.values)
        )

    def getLast(count=1000):
        reversed(self.items)[:count]

    def printLast(count=1000):
        for entry in self.getLast(count):
            print("{0}: {2} - timeSinceCreated: {1}".format(entry[0], time.monotonic() - entry[1], entry[2]))
