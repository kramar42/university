#! /usr/bin/env python


from random import randint
from math import sqrt, pi, e
from decimal import Decimal
from sequence import to_digits
from itertools import izip


tau = Decimal(2*pi)
e = Decimal(e)


def fact(n):
    return Decimal(sqrt(tau*n))*(n/e)**n


def conflicts_criteria(sequence, m):
    n = len(sequence)
    c = len(sequence) - len(set(sequence))

    numinator = fact(m)*fact(n)
    denominator = fact(m-n+c)*(m**n)*fact(n-c)*fact(c)

    return numinator / denominator


def polynom_criteria(random, m=0):
    p = 7
    k = 4
    n = 50
    A = [1, 3, 1, 5]
    X = [k for i,k in izip(xrange(n), random)]
    for i in xrange(k-1, n):
        for j in xrange(1, k):
            X[i] += A[j] * X[i-j] % p
    return p ** k - 1


def permutations_criteria(sequence, t):
    r = t - 1
    f = 0

    while r > 0:
        print 'Next iteration...'
        m = sequence[0]
        s = 0
        for i in range(1, r):
            if sequence[i] > m:
                s = i
                m = sequence[s]
        f = r * f + s - 1

        print 'Swapping elements ', r, ' and ', s, '...'
        tmp = sequence[r]
        sequence[r] = sequence[s]
        sequence[s] = tmp

        r = r - 1
    return f


def main():
    n = 2**14
    m = 2**20

    sequence = list()
    for _ in xrange(n):
        sequence.append(randint(0,m))

    print permutations_criteria(sequence, len(sequence))

if __name__ == '__main__':
    main()

