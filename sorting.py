
import random
import heapq

def quick_sort(seq):
    if len(seq) == 0:
        return seq
        
    pivot = seq[0]
    lower = []
    higher = []
    for item in seq[1:]:
        if item < pivot:
            lower.append(item)
        else:
            higher.append(item)

    output = quick_sort(lower)
    output.append(pivot)
    output.extend(quick_sort(higher))
        
    return output

def heap_sort(seq):
    heapq.heapify(seq) # O(N)
    output = []
    while seq:
        output.append(heapq.heappop(seq))
    return output

class Heap(object):
    def __init__(self):
        self.tree = []
        
    def insert(self, item):
        self.tree.append(item)
        i = len(self.tree) - 1
        par = (i - 1)//2
        while par >= 0 and self.tree[par] > item:
            print i, par
            self.tree[par], self.tree[i] = self.tree[i], self.tree[par]
            i = par
            par = (i - 1)//2

    def pop(self):
        """This is not quite right, yet.
        """
        val = self.tree[0]
        i = 0
        c1, c2 = 2*i + 1, 2*i + 2
        n = len(self.tree)
        
        while i < n:
            if c1 >= n:
                # last element
                c1_val = None
                c2_val = None
            else:
                c1_val = self.tree[c1]
                c2_val = self.tree[c2]
                
            if c1_val < c2_val or c2_val is None:
                self.tree[i] = c1_val
                i = c1
            else:
                self.tree[i] = c2_val
                i = c2
                
            c1, c2 = 2*i + 1, 2*i + 2
            
        return val
                                         

def heap_sort2(seq):
    h = Heap()
    for item in seq:
        h.insert(item)
    

seq = [45, 89, 38, 51, 97, 37, 26, 46, 10, 48, 81, 20, 78, 41, 59, 42, 19, 89, 87, 92, 39, 46, 32, 19, 78, 66, 11, 14, 99, 51, 41, 98, 67, 62, 41, 20, 40, 28, 73, 7, 86, 70, 85, 5, 20, 3, 71, 86, 2, 34, 80, 87, 45, 66, 64, 95, 18, 85, 27, 66, 24, 55, 27, 67, 72, 55, 10, 23, 50, 69, 42, 90, 68, 29, 37, 12, 43, 81, 53, 42, 89, 88, 27, 18, 52, 41, 65, 17, 79, 59, 90, 57, 18, 72, 88, 64, 61, 27, 38, 29]
    
def test():
    sorted_seq = sorted(seq)
    assert sorted_seq == quick_sort(seq)
    assert sorted_seq == heap_sort(seq)
    
    

if __name__ == '__main__':
    test()
