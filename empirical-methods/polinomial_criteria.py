#! /usr/bin/env python

def polynom(random):
    p = 7
    k = 4
    n = 50
    A = [1, 3, 1, 5]
    X = [k for i,k in zip(range(n), random)]
    for i in xrange(k-1, n):
        for j in xrange(1, k):
            X[i] += A[j] * X[i-j] % p
    return p ** k - 1
