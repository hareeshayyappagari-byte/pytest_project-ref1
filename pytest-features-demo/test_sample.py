def add(a,b):
    return a+b

def mul(a,b):
    return a*b


def is_even_or_odd(n):
    if n % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

def test_methods_add_and_mul():
    assert add(1,2) == mul(3,1)


def test_even_or_odd(n=5):
    if n % 2 == 0:
        print("even number")
    else:
        print("odd number")

def test_large_even_numbers():
    result = is_even_or_odd(100000000)
    assert result == "EVEN" , "100000000 should be ODD ..."