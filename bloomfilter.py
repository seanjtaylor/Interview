
import math
from bitarray import bitarray

class BF(object):
    def __init__(self, nbits=2**8):
        self.nbits = nbits
        self.ba = bitarray(nbits)
        self.ba[:] = False
        self.items = 0
        self.n_hashes = 1

    def add(self, obj):
        self.ba[hash(obj) % self.nbits] = True
        self.items += 1

    def __contains__(self, obj):
        return self.ba[hash(obj) % self.nbits]
    
    def false_positive_rate(self):
        p = (1 - math.exp(-(self.n_hashes*self.items) /
                          float(self.nbits)))**self.n_hashes
        return p
        
        
