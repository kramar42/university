#! /usr/bin/env python

from random import randint
from itertools import izip
import math
from levin_method import levin
from marsalia_method import marsalia

class mclaren_marsalia:
        def __init__(self, method1, method2, r):
            self.r = r
            self.method1 = method1
            self.method2 = method2
            self.xi = [int(math.fabs(x)) for _,x in izip(xrange(r), method1)]
            self.yi = [int(math.fabs(y)) for _,y in izip(xrange(r), method2)]
            self.A = self.xi[:]
            self.my = max(self.yi)

        def updateCurrentXiYi(self):
            self.currentXi = self.xi[randint(0,self.r-1)]
            self.currentYi = self.yi[randint(0,self.r-1)]

        def __iter__(self):
            return self

        def next(self):
            self.updateCurrentXiYi()
            j = int(math.fabs((self.r-1) * self.currentYi / self.my))
            nextNumber = self.A[j]
            self.A[j] = self.currentXi;
            return nextNumber

def period (a, b):
    return a / gcd(a, b) * b

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    l = levin(238490123, 12049912)
    m = marsalia(12839041)
    r = mclaren_marsalia(l, m, 100)
    for _,k in izip(xrange(10), r):
        print k

if __name__ == '__main__':
    main()

