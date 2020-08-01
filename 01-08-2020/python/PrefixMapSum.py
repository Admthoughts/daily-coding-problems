class PrefixMapSum():

    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        if len(key) > 3:
            pref = key[3:]
        else:
            pref = key
        
        return pref

    def sum(self, pref):
        pass        