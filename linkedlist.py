
# Linked Lists

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList(object):
    def __init__(self, seq=None):
        self.length = 0
        self.last = None
        
        if not seq:
            self.first = None
            return
        
        self.last = None
        for val in seq:
            self.length += 1
            if not self.last:
                self.first = Node(val)
                self.last = self.first
            else:
                self.last.next = Node(val)
                self.last = self.last.next
                
    def __repr__(self):
        node = self.first
        vals = []
        while node:
            vals.append(str(node.value))
            node = node.next
        return '[%s]' % ','.join(vals)
        
    def append(self, val):
        self.last.next = Node(val)
        self.length += 1
        
    def insert(self, pos, val):
        node = self.first
        while pos > 0:
            node = node.next
            pos -=1
            
        new_node = Node(val, node.next)
        node.next = new_node
        
        self.length += 1
        
    def __len__(self):
        return self.length
                