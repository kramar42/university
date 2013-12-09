#! /usr/bin/env python

from itertools import izip

class marsalia:
    def __init__(self, seed):
        self.m = 2 ** 23
        self.seed = seed
        self.buf = [seed + i for i in xrange(55)]

    def __iter__(self):
        return self

    def next(self):
        x = (self.buf[55 - 24] * self.buf[55 - 55]) % self.m
        del self.buf[0]
        self.buf.append(x)
        return x


def main():
    m = marsalia(12839041)
    for _,k in izip(xrange(10), m):
        print k

if __name__ == '__main__':
    main()
