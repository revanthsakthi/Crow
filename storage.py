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
    def get(self, key, value, default_value=None):
        raise NotImplementedError
