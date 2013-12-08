#! /usr/bin/env python

from random import randint

class MacLarena_MarsaliiMethod:
    def __init__(self, m, r):
        self.m = m
        self.r = r

    def generator(self):
        numbers = []
        arrayX = self.createRInt()

        while True:
            x = randint(0, self.m)
            y = randint(0, self.m)
            j = self.r * y / self.m
            yield arrayX[j]
            arrayX[j] = x

    def createRInt(self):
        return [randint(0, self.m) for _ in range(self.r)]

def main():
    r = MacLarena_MarsaliiMethod(10, 42).generator()
    for i,k in zip(range(10), r):
        print k

if __name__ == '__main__':
    main()

