#! /usr/bin/env python

import sys
import random
import math
from itertools import izip

class levin:
    def __init__(self, seed, modulus):
        self.seed = seed
        self.currentX = seed
        self.modulus = modulus
        self.t = self.constant()

    def __iter__(self):
        return self

    def next(self):
        self.currentX = self.currentX ** 2 % self.modulus
        return (self.currentX * ScalarMutiplexBinary(self.currentX, self.t) % 2)

    def constant(self):
        seed = random.randint(0, sys.maxint)
        operand = (1 << int(math.log(self.modulus) / math.log(2) + 1)) - 1
        return seed & operand

def ScalarMutiplexBinary(first, second):
    return len(filter(lambda c: c=='1', bin(first & second)))

def main():
    l = levin(12348101, 12049912)
    for _,k in izip(xrange(50), l):
        print k,

if __name__ == '__main__':
    main()

