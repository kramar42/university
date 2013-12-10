#! /usr/bin/env python
# -*- encoding: utf-8 -*-

# sys.maxint == 2 * 63
# 2 ** 63 - 1 == 7**2 * 73 * 127 * 337 * 92737 * 649657
# 2 ** 63 + 1 == 3 ** 3 * 19 * 43 * 5419 * 77158673929

# Выбор модуля.
# Максимальное число помещающееся в машинное слово - 1
# Максимальное просто число меньше w

# b = a - 1 кратно каждому простому делителю m
# и b должно быть кратоно 4, если m кратно 4

from itertools import izip

class lincong:
    def __init__(self, m, a, c, seed):
        self.m = m
        self.a = a
        self.c = c
        self.x = seed

    def __iter__(self):
        return self

    def next(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def potential(self, bound=100):
        potent = 0
        accum = (self.a - 1)
        for i in xrange(bound):
            if accum % self.m == 0:
                return potent
            accum *= (self.a - 1)
            potent += 1
        return None

def main():
    l = lincong(2**63, 2**11+1, 2**27+1, 1238417890234)
    seq = (k for _,k in izip(xrange(20), l))
    print 'Sequence:',
    for e in seq:
        print e,
    print '\nPotential:', l.potential(100000)

if __name__ == '__main__':
    main()
