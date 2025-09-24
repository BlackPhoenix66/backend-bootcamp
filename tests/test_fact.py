from factorials import factorial_iter, factorial_rec

def test_factorial_small():
    assert factorial_iter(5) == 120
    assert factorial_rec(5) == 120

def test_factorial_zero():
    assert factorial_iter(0) == 1
    assert factorial_rec(0) == 1