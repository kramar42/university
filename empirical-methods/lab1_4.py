#! /usr/bin/env python

import math

class KoveyMethod:
    def __init__(self, seed):
        self.x = seed
        self.seed = seed
        self.l = 15

    def getNext(self):
        self.x = self.x * (self.x + 1) % int(2 ** self.l)
        return int(math.fabs(self.x))

def main():
    r = KoveyMethod(42)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

