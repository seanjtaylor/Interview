
# Bit arrays

def ba_and(x, y):
    return [i and j for i, j in zip(x, y)]
    
def test_ba_and():
    assert ba_and([0,1,0,1],[1,0,0,1]) == [0,0,0,1]
    
def ba_or(x, y):
    return [i or j for i, j in zip(x, y)]
    
def test_ba_or():
    assert ba_or([0,1,0,1],[1,0,0,1]) == [1,1,0,1]
