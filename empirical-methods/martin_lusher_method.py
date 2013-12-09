#! /usr/bin/env python

from marsalia_method import marsalia
from itertools import izip

class martin_lusher:
    def __init__(self, marsalia, marsalia_N, lusher_N):
        self.marsalia_N = marsalia_N
        self.lusher_N = lusher_N
        self.marsalia = marsalia
        self.counter = 0

    def generateMarsaliaNumbers(self):
        self.numbers = [k for i,k in zip(range(self.marsalia_N), self.marsalia)]
        self.counter = self.lusher_N

    def __iter__(self):
        return self

    def next(self):
        if self.counter == 0:
            self.generateMarsaliaNumbers()
        nextNumber = self.numbers[0]
        del self.numbers[0]
        self.counter -= 1
        return nextNumber

def main():
    m = marsalia(315812035)
    ml = martin_lusher(m, 17, 10)
    for _,k in izip(xrange(10), ml):
        print k

if __name__ == '__main__':
    main()

