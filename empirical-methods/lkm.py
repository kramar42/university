#! /usr/bin/env python

import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lkm(x0, m, c, a, n):
    n = 1600
    A = [0] * n
    period = 1
    A[0] = x0 % m

    for i in xrange(n):
        A[i] = (a * A[i - 1] + c) % m

    if gcd(c, m) == 1 and ((a-1) % m) == 0 and (m % 4) == 0 and ((a-1) % 4) == 0:
        period = m

    for j in xrange(1, n):
        if A[0] == A[j]:
            period = j

    potencial = math.log(period) / math.log(a - 1)
    return A

def main():
    l = lkm(418902, 234810234, 231480, 1249912, 5)
    for i in l:
        print i

if __name__ == '__main__':
    main()
