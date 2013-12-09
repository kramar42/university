#! /usr/bin/env python

import math
from itertools import izip

class KoveyMethod:
    def __init__(self, seed):
        self.x = seed
        self.seed = seed
        self.l = 15

    def __iter__(self):
        return self

    def next(self):
        self.x = self.x * (self.x + 1) % int(2 ** self.l)
        return int(math.fabs(self.x))

def main():
    r = KoveyMethod(42)
    for _,k in izip(xrange(10), r):
        print k

if __name__ == '__main__':
    main()

