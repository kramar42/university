#! /usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def fibanachi(a, b, m):
    first = a % m
    yield first
    second = b % m
    yield second
    while True:
        (first, second) = (second, first+second)
        yield second

def period(X, mx):
    for i in xrange(mx):
        for j in xrange(1, mx-1):
            if X[i] == X[j] and X[i + 1] == X[j + 1]:
                px = j - i
                if px != 0:
                    z = True
                    break
        if z:
            break
    return px

def posl(mx, my):
    X = [0] * mx
    Y = [0] * my
    W = [0] * my
    X = fibanachi(4589,8459,mx,mx)
    Y = fibanachi(215,4856,mx,my)
    px = periodx(X,mx)
    py = periody(Y,my)

    for i in xrange(my):
        W[i] = (X[i] + Y[i]) % mx
    if gcd(px, py) == 1:
        pw = px * py
    else:
        for i in xrange(my):
            for j in xrange(1, my-1):
                if W[i] == W[j] and W[i + 1] == W[j + 1]:
                    pw = j - i
                    if pw != 0:
                        z = True
                        break
            if z:
                break
