#function usage: n choose k = choose(n,k)
def choose( n, k):
    return fact(n)/(fact(k)*fact(n-k))

#is factorial ya
def fact(val):
    if val < 1:
        return -1
    if val is 1:
        return 1
    else:
        return val*fact(val-1)


