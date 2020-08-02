class PrefixMapSum():

    def __init__(self):
        self.keymap = {}

    def insert(self, key, val):
        self.keymap[key] = val

    def sum(self, key):
        if len(key) > 3:
            pref = key[:3]
        else:
            pref = key

        valList = []
        for k, v in self.keymap.items():
            if k[:3] == pref:
                valList.append(v)
        
        return sum(valList)