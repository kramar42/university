#! /usr/bin/env python

from itertools import izip

class fon_neiman():
    def __init__(self, x):
        self.x = x
        self.s = str(x)
        self.size = len(self.s)

    def __iter__(self):
        return self

    def next(self):
        s = str(self.x ** 2)
        diff = len(s) - self.size
        shift = diff / 2

        s = s[shift: -(diff - shift)]
        self.x = int(s)
        return self.x


def main():
    f = fon_neiman(1234567890)
    for _,k in izip(xrange(10), f):
        print k

if __name__ == '__main__':
    main()
