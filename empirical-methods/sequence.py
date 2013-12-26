#! /usr/bin/env python

from itertools import izip
from math import fabs


def to_digits(value):
    return map(lambda c: ord(c) - ord('0'), list(str(value)))


def to_number(array):
    return reduce(lambda a,x: a*10+x, array)


def take(method, count):
    return (k for _,k in izip(xrange(count), method))


def join_sequence(xiterator, yiterator, length=None, seed=2**63-1, plus=True):
    if isinstance(xiterator, list):
        xlist = xiterator
    else:
        xlist = [k for _,k in izip(xrange(length), xiterator)]
    x = xlist[int(fabs(seed) % len(xlist))]
    if plus:
        func = lambda x: int(fabs((x + yiterator.next()) % len(xlist)))
    else:
        func = lambda x: int(fabs((x - yiterator.next()) % len(xlist)))
    while True:
        x = xlist[func(x)]
        yield x


class period:
    def __init__(self, generator):
        self.generator = generator

    def find(self, accuracy=1000):
        numbers = []
        while True:
            firstMatch = next(self.generator)
            if firstMatch in numbers:
                index = numbers.index(firstMatch)
                numbers.append(firstMatch)
                stopped = len(numbers)
                flag = True
                for i in xrange(1, accuracy):
                    nextMatch = next(self.generator)
                    numbers.append(nextMatch)
                    if numbers[index + i] != nextMatch:
                        flag = False
                        break
                if flag:
                    return stopped - index - 1
            else:
                numbers.append(firstMatch)
            if len(numbers) >= accuracy ** 2:
                return None


def main():
    from generator import knut

    p = period(knut(1283494))
    print p.find()

if __name__ == '__main__':
    main()

