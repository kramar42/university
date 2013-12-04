#! /usr/bin/env python

from random import randint

class MacLarena_MarsaliiMethod:
    def __init__(self, k, m, r):
        self.k = k
        self.m = m
        self.r = r

    def getList(self):
        numbers = []
        arrayX = self.createRInt()

        for i in range(k):
            x = randint(0, self.m)
            y = randint(0, self.m)
            j = r * y / self.m
            numbers.append(arrayX[j])
            arrayX[j] = x

        return numbers

    def createRInt(self):
        return [randint(0, self.m) for _ in range(selr)]

def main():
    r = MacLarena_MarsaliiMethod(10, 42, 100)
    for i in r:
        print i

if __name__ == '__main__':
    main()

