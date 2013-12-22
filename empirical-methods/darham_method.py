#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import random
import math
from levin_method import levin
from itertools import izip

class darham:
    def __init__(self, method, r):
        self.r = r
        self.method = method
        self.generate_xi()
        self.xi = make_positive(self.xi)
        self.mx = max(self.xi)

    def generate_xi(self):
        self.xi = [x for i, x in zip(range(self.r), self.method)]
        self.a = self.xi[:]

    def update_xi(self):
        self.current_xi = self.xi[random.randint(0, self.r-1)]

    def getSeed(self):
        return self.current_xi

    def getT(self, period):
        return self.period

    def __iter__(self):
        return self

    def next(self):
        self.update_xi()
        j = int(math.floor(math.fabs((self.r-1) * self.current_xi / self.mx)))
        nextnum = self.a[j]
        self.a[j] = self.current_xi
        return nextnum


def make_positive(x):
    return map(lambda n: int(math.fabs(n)), x)


def main():
    l = levin(12348101, 1249912)
    d = darham(l, 10)
    for _,k in izip(xrange(10), d):
        print k

if __name__ == '__main__':
    main()
