#! /usr/bin/env python

import math

class Digits:
        def __init__(self, value):
            self.digits = map(lambda c: ord(c) - ord('0'), list(str(value)))

        def getValue(self):
            return reduce(lambda a,x: a*10+x, self.digits)

        def nextMax(self):
            return self.digits.pop()

class KnutMethod:
    def __init__(self, seed):
        self.x = seed
        self.seed = seed
        self.digits = Digits(self.x)

    def getSeed(self):
        return self.seed

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
        currentDigits = Digits(self.x)
        for j in range(len(currentDigits.digits)):
            if 0 != currentDigits.digits[j]:
                currentDigits.digits[j] -= 1
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
        self.digits = Digits(self.x)

    def getNext(self):
        counter = self.digits.nextMax()
        for i in range(counter+1):
            case = self.digits.nextMax() + 3
            if case == 3:
                self.case3()
            elif case == 4:
                self.case4()
            elif case == 5:
                self.case5()
            elif case == 6:
                self.case6()
            elif case == 7:
                self.case7()
            elif case == 8:
                self.case8()
            elif case == 9:
                self.case9()
            elif case == 10:
                self.case10()
            elif case == 11:
                self.case11()
            elif case == 12:
                self.case12()
        return int(math.fabs(self.x))

def main():
    r = KnutMethod(42)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

