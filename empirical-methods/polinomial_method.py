#! /usr/bin/env python

import random
import sys

class PolinomialMethod:
    def __init__(self, seed):
        self.seed = seed
        self.p = 5
        self.k = 4
        self.a = [2,3,0,1]

        self.buf = []
        for i in range(self.k):
            self.buf.append(random.randint(0,sys.maxint))

    def getNext(self):
        x = 0
        for j in range(self.k):
            x += self.a[j] * self.buf[self.k - j - 1] % self.p
        del self.buf[0]
        self.buf.append(x)
        return x

def main():
    r = PolinomialMethod(42)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

