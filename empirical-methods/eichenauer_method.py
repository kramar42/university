#! /usr/bin/env python

import sys
import math
from itertools import izip

class EichenauerMethod:
    def __init__(self, a, c, m, seed):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def __iter__(self):
        return self

    def next(self):
        if self.x == 0:
            self.x = sys.maxint
        else:
            self.x = (evklid(self.a, self.x, self.m) + self.c) % self.m
        return self.x

def evklid(u, v, m):
    A = 1
    B = 0
    D = 1

    while v != 0:
        q = int(math.floor(u / v))
        t1 = u - q * v
        t3 = B - q * D
        u = v
        B = D
        v = t1
        D = t3

    d = u
    x = A
    y = B

    if y >= 0:
        return y
    else:
        return int(math.fabs(y + m))

def main():
    r = EichenauerMethod(25454549, 24, 5757, 9090)
    for _,k in izip(xrange(10), r):
        print k

if __name__ == '__main__':
    main()
