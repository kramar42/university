#! /usr/bin/env python

import math
from itertools import izip

class digits:
        def __init__(self, value):
            self.digits = map(lambda c: ord(c) - ord('0'), list(str(value)))

        def getValue(self):
            return reduce(lambda a,x: a*10+x, self.digits)

        def nextMax(self):
            return self.digits.pop()

class knut:
    def __init__(self, seed):
        self.x = seed
        self.seed = seed
        self.digits = digits(self.x)
    
    def __iter__(self):
        return self.iterator()

    def case3(self):
        if self.x < 5000000000L:
            self.x += 5000000000L
        self.case4()
    def case4(self):
        self.x = int(math.floor((self.x * self.x) / 100000L)) % 10000000000L
        self.case5()
    def case5(self):
        self.x = int(math.floor((self.x * self.x) / 100000L)) % 10000000000L
        self.case6()
    def case6(self):
        if self.x < 100000000L:
            self.x += 9814055677L
        else:
            self.x = 10000000000L - self.x
        self.case7()
    def case7(self):
        first5 = self.x % 100000
        self.x = first5 * 100000 + (self.x / 100000)
        self.case8()
    def case8(self):
        self.x = (1001001001L * self.x) % 10000000000L
        self.case9()
    def case9(self):
        currentDigits = digits(self.x)
        for j in range(len(currentDigits.digits)):
            if 0 != currentDigits.digits[j]:
                currentDigits.digits[j] -= 1
        self.x = currentDigits.getValue()
        self.case10()
    def case10(self):
        if self.x < 100000L:
            self.x = self.x * self.x + 99999L
        else:
            self.x -= 99999L
            self.case11()
    def case11(self):
        while self.x < 1000000000L:
            self.x *= 10
        self.case12()
    def case12(self):
        self.x = int(math.floor((self.x * (self.x - 1) / 100000L))) % 10000000000L
        self.digits = digits(self.x)

    def iterator(self):
        while True:
            counter = self.digits.nextMax()
            for i in xrange(counter+1):
                case = self.digits.nextMax() + 3
                getattr(self, 'case' + str(case))()
            yield (int(math.fabs(self.x)))

def main():
    kn = knut(1283494)
    for _,k in izip(xrange(10), kn):
        print k

if __name__ == '__main__':
    main()

