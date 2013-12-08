#! /usr/bin/env python

from knut_method import Knut
import itertools

class Period:
    def __init__(self, accuracy):
        self.accuracy = accuracy

    def find(self, generator):
        numbers = []
        while True:
            firstMatch = next(generator)
            if firstMatch in numbers:
                index = numbers.index(firstMatch)
                numbers.append(firstMatch)
                stopped = len(numbers) - 1
                flag = True
                for i in xrange(self.accuracy):
                    nextMatch = next(generator)
                    numbers.append(nextMatch)
                    if numbers[index + i] != nextMatch:
                        flag = False
                        break
                if flag:
                    return stopped - index
            else:
                numbers.append(firstMatch)
            if len(numbers) >= 10000:
                return 10000


def main():
    knut = Knut(100).iterator()
    generator = itertools.cycle(range(12))
    for i, k in zip(range(20), generator):
        print k
    period = Period(1000)
    print period.find(generator)

if __name__ == '__main__':
    main()
