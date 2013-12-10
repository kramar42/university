#! /usr/bin/env python

import math
from itertools import izip

class kovey:
    def __init__(self, seed):
        self.x = seed
        self.seed = seed
        self.l = 15

    def __iter__(self):
        return self

    def next(self):
        self.x = self.x * (self.x + 1) % 2 ** self.l
        return self.x

def main():
    k = kovey(32849102834)
    for _,k in izip(xrange(100), k):
        print k,

if __name__ == '__main__':
    main()

