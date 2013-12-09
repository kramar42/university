#! /usr/bin/env python

from itertools import izip

class quadkong:
    def __init__(self, d, m, a, c, seed):
        self.d = d
        self.m = m
        self.a = a
        self.c = c
        self.x = seed

    def __iter__(self):
        return self

    def next(self):
        self.x = (self.d * self.x ** 2 + self.a * self.x + self.c) % self.m
        return self.x

def main():
    q = quadkong(2**62+1, 2**63-1, 2**62+1, 2**61+1, 1238417890234)
    for _,k in izip(xrange(20), q):
        print k

if __name__ == '__main__':
    main()
