#! /usr/bin/env python

from levin_method import levin
from knut_method import knut

class Random:
    def __init__(self, seed, g):
        self.m = levin(seed * 892412, 28 ** seed);
        self.k = knut(seed % 42210).iterator()
        self.seed = seed

    def __iter__(self):
        return self

    def next(self):
        self.seed += self.k.next()
        self.seed -= self.m.next()
        self.x = self.seed
        return self.x

def main():
    r = Random(42, 294)
    for i, k in zip(range(10), r):
        print k

if __name__ == '__main__':
    main()
