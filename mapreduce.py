
import itertools
# Fake MR framework that does everything sequentially

class MR(object):
    def __init__(self, inp):
        self.input = inp
        self.map_output = {}
        self.reduce_output = []
        
    def run(self):
        for key, value in self.input:
            self.map(key, value)

        for key, values in self.map_output.iteritems():
            self.reduce(key, values)


    def map_emit(self, key, value):
        if key in self.map_output:
            self.map_output[key].append(value)
        else:
            self.map_output[key] = [value]

    def reduce_emit(self, value):
        self.reduce_output.append(value)
        
    def map(self, key, value):
        self.map_emit(key, value)

    def reduce(self, key, values):
        self.reduce_emit(key)


data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]

class WordCount(MR):
    def map(self, key, value):
        for word in value.split():
            self.map_emit(word, 1)

    def reduce(self, key, values):
        self.reduce_emit((key, sum(values)))


def test1():
    wc = WordCount(enumerate(data))
    wc.run()
    print wc.reduce_output
        

class NumNeighbors(MR):
    def map(self, key, value):
        i, j = value
        self.map_emit(i, 1)
        self.map_emit(j, 1)
    def reduce(self, key, values):
        self.reduce_emit((key, sum(values)))

def test2():
    edges = (map(int, s.strip().split(','))
             for s in open('edges.csv').readlines())
    fn = NumNeighbors(enumerate(edges))
    fn.run()

# Triange Counting (Suri and Vassilvitskii 2011)

class Step1(MR):
    def map(self, key, value):
        i, j = key
        self.map_emit(i, j)
        
    def reduce(self, key, values):
        # emit all edges that would create triangles that include :key:
        for value1 in values:
            for value2 in values:
                self.reduce_emit((key, (value1, value2)))

class Step2(MR):
    def map(self, key, value):
        if value is None:
            i, j = key
            # None is a sentinel here to indicate this edge exists
            self.map_emit((i, j), None) 
        else:
            i, j = value
            # emit edges where if they existed, the nodes would be in triangles
            self.map_emit((i, j), key) 
        
    def reduce(self, key, values):
        if None not in values:
            return # necessary edge does not exist

        # necessary edge does exist, emit the nodes and 1 for "is part of tri"
        for value in values:
            if value is None: continue
            self.reduce_emit((value, 1))

class Step3(MR):
    def map(self, key, value):
        self.map_emit(None, 1)
        
    def reduce(self, key, values):
        self.reduce_emit(sum(values))
            
def test3():
    edges = (map(int, s.strip().split(','))
             for s in open('edges.csv').readlines())


    s1 = Step1((e, None) for e in edges)
    s1.run()

    edges = (map(int, s.strip().split(','))
             for s in open('edges.csv').readlines())

    s2 = Step2(itertools.chain(((e, None) for e in edges), s1.reduce_output))
    s2.run()

    print s2.reduce_output[:10]

    s3 = Step3(s2.reduce_output)
    s3.run()
    print s3.reduce_output
