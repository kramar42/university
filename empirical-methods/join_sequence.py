#! /usr/bin/env python

from itertools import izip
import math
import random
from knut_method import knut

def join_sequence(xiterator, yiterator, length=None, seed=2**63-1, plus=True):
    if isinstance(xiterator, list):
        xlist = xiterator
    else:
        xlist = [k for i,k in izip(xrange(length), xiterator)]
    x = xlist[int(math.fabs(seed) % len(xlist))]
    if plus:
        func = lambda x: int(math.fabs((x + yiterator.next()) % len(xlist)))
    else:
        func = lambda x: int(math.fabs((x - yiterator.next()) % len(xlist)))
    while True:
        x = xlist[func(x)]
        yield x


def main():
    first = map(lambda x: random.randint(0, 10000), range(100))
    second = knut(1283494).iterator()
    for _,k in izip(xrange(10), join_sequence(first, second)):
        print k


if __name__ == '__main__':
    main()

