#! /usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def kkm(d, x0, a, c, m, n):
    A = [0] * n
    period = 0

    A[0] = x0 % m
    for i in xrange(1, n):
        A[i] = (d * A[i - 1] * A[i-1] + a * A[i-1] + c) % m

    if gcd(c, m) == 1 and ((a - 1) % m) == 0 and (d % m) == 0 and (d % 2) == 0 and (d % 4 == (a-1) % 4) \
            and (d % 2 == (a - 1) % 2) and (d % 9 != (3*c) % 9):
        period = m

    for j in xrange(1, n):
        if A[0] == A[j]:
            period = j

    return A

def main():
    k = kkm(418902, 234810234, 21490, 231480, 1249912, 10)
    for i in k:
        print i

if __name__ == '__main__':
    main()
