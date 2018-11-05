def choose(n, k):
    return fact(n) / (fact(k) * fact(n - k))


# def test(a):
#    print(_fact(5))

def fact(val):
    if val < 1:
        return -1
    if val is 1:
        return 1
    else:
        return val * fact(val - 1)

# test(5)
