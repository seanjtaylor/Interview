
import random
# randrange does not include endpoint. e.g. randrange(2) -> {0,1}

def sample(seq, n=10):
    s = []
    for i, val in enumerate(seq):
        if i < n:
            s.append(val) # fill the reservoir
            continue

        # should be n/(i+1) chance of inclusion
        draw = random.randrange(i+2)
        if draw < n:
            # a reservoir item is removed with (1/n) * ( n / (i+1)) 
            # so sample prob is i/(i+1)
            s[draw] = val
            
    return s

def mean(seq):
    s = 0
    for i, val in enumerate(seq):
        s += val
    return s / float(i+1)
        

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Reservoir Sampling')
    parser.add_argument('--n', dest='n', action='store', type=int, default=10)
    parser.add_argument('infile', nargs='?', default=sys.stdin,
                        type=argparse.FileType('r'))
    parser.add_argument('outfile', nargs='?', default=sys.stdout,
                        type=argparse.FileType('w'))
    args = parser.parse_args()
    def seq():
        line = args.infile.readline()
        while line:
            yield int(line)
            line = args.infile.readline()
            
    for val in sample(seq(), args.n):
        args.outfile.write('%i\n' % val)
