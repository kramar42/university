#! /usr/bin/env python

class LinKongMethod:
    def __init__(self, a, c, m, seed):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def getNext(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def Potential(self):
        s = 0
        while (self.a - 1)**s % self.m != 0 and s < 100000:
            s += 1
        return s

def main():
    r = LinKongMethod(19, 23, 29, 31)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

