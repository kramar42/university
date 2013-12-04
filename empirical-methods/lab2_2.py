#! /usr/bin/env python

from random import randint
from math import sqrt, pi, e
from decimal import Decimal

tau = Decimal(2*pi)
e = Decimal(e)

def criteria(sequence, m):
    n = len(sequence)
    c = conflicts(sequence)

    numinator = fact(m)*fact(n)
    denominator = fact(m-n+c)*(m**n)*fact(n-c)*fact(c)

    print c, n, m
    return numinator / denominator

def conflicts(sequence):
    return len(sequence) - len(set(sequence))

def fact(n):
    return Decimal(sqrt(tau*n))*(n/e)**n

def main():
    n = Decimal(2**14)
    m = Decimal(2**20)

    sequence = list()
    for _ in range(n):
        sequence.append(randint(0,m))

    print criteria(sequence, m)


if __name__ == '__main__':
    main()

