#! /usr/bin/env python

from itertools import izip

class mochli:
    def __init__(self, first, second, k, module):
        self.module = module
        self.first = first
        self.second = second
        self.k = k

    def generator(self):
        # returning first 2 elements from sequence
        yield (self.first)
        yield (self.second)

        for i in xrange(2, self.k+1):
            self.first, self.second = self.second, (self.first + self.second) % self.module
            yield (self.second)
        for i in xrange(k+1, self.n):
            self.A[i] = (self.A[i-1] + self.A[i-k]) % self.m
            yield (self.A[i])


def main():
    j = mochli(418902, 21490, 231480, 1249912).generator()
    for _,k in izip(xrange(10), j):
        print k

if __name__ == '__main__':
    main()
