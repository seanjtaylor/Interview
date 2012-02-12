
# Uses Chaining to deal with collisions
# Everything works except delete item is having some trouble

class HT(object):
    def __init__(self, size=2**8):
        self.table = [None]*size
        self.size = size

    def __setitem__(self, key, value):
        ix = hash(key) % self.size
        val = self.table[ix]
        if val is None:
            self.table[ix] = [[key, value]] # must store the key as well
        else:
            is_set = False
            for j, (k, v) in enumerate(self.table[ix]):
                if key == k:
                    self.table[ix][j][1] = value
                    is_set = True
            if not is_set:
                self.table[ix].append([key, value])

    def __getitem__(self, key):
        ix = hash(key) % self.size
        val = self.table[ix]
        if not val:
            raise KeyError
        for k, v in self.table[ix]:
            if key == k:
                return v
        raise KeyError

    def __delitem__(self, key):
        ix = hash(key) % self.size
        to_remove = None
        for i, (k, v) in enumerate(self.table[ix] or ()):
            if key == k:
                to_remove = i
        if to_remove is None:
            raise KeyError
        else:
            l = self.table[ix]
            self.table[ix] = l[:i] + l[i+1:]
            
        
