
import random
        

# Integer operations

def count_of(seq, test=lambda x: True):
    # O(N)
    counter = 0
    for val in seq:
        if test(val):
            counter += 1
    return counter
    
def test_count_of():
    seq = range(1000)
    assert count_of(seq, lambda x: x == 4) == 1
    assert count_of(seq, lambda x: x % 10 == 0) == 100
    
# Find smallest number

def smallest(seq):
    # O(N)
    m = None
    for val in seq:
        if m is None or val < m:
            m = val
    return m
    
def test_smallest():
    seq = [random.randrange(0,1000) for i in range(100)]
    assert min(seq) == smallest(seq)

def largest(seq):
    return -smallest(-s for s in seq)
    
def test_largest():
    seq = [random.randrange(0,1000) for i in range(100)]
    assert max(seq) == largest(seq)

def is_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True
    
def test_is_palindrome():
    assert is_palindrome(11211)
    assert not is_palindrome(11212)
    assert is_palindrome(123321)
    assert not is_palindrome(123221)
    
def closest_palindrome(n):
    s = list(str(n))
    for i in range(len(s) // 2):
        s[-(i+1)] = s[i]
    return int(''.join(s))
    
def test_closest_palindrome():
    assert closest_palindrome(112233) == 112211
    for i in range(10):
        n = random.randrange(0,100000)
        assert is_palindrome(closest_palindrome(n))
        
    