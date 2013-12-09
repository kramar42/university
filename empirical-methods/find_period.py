#! /usr/bin/env python

from levin_method import levin

class period:
    def __init__(self, generator):
        self.generator = generator

    def find(self, accuracy):
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
    l = levin(12348101, 12049912)
    p = period(l)
    print p.find(1000)

if __name__ == '__main__':
    main()
