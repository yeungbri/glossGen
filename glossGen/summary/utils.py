def ALL(x):
    return True

def getZero():
    return 0

class DefaultDict():

    def __init__(self, initialize=getZero):
        self._dict = {}
        self._initialize = initialize

    def __getitem__(self, key):
        if key in self._dict:
            return self._dict[key]
        else:
            self._dict[key] = self._initialize()
            return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def update(self, other):
        self._dict.update(other.asDict())

    def asDict(self):
        # Make a copy of the internal dict
        return dict(self._dict)

    def copy(self):
        copy = DefaultDict(initialize=self._initialize)
        copy._dict = self.asDict()
        return copy

    def filtered(self, key_pred=ALL, val_pred=ALL):
        filtered = {}
        for key, val in self._dict.items():
            if key_pred(key) and val_pred(val):
                filtered[key] = val

        return filtered
