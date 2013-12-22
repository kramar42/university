#! /usr/bin/env python

from itertools import repeat, izip
import math
import random
from generator import knut


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def fibanachi(a, b, m):
    first = a % m
    yield first
    second = b % m
    yield second
    while True:
        (first, second) = (second, first+second)
        yield second

def period(X, mx):
    for i in xrange(mx):
        for j in xrange(1, mx-1):
            if X[i] == X[j] and X[i + 1] == X[j + 1]:
                px = j - i
                if px != 0:
                    z = True
                    break
        if z:
            break
    return px

def posl(mx, my):
    X = [0] * mx
    Y = [0] * my
    W = [0] * my
    X = fibanachi(4589,8459,mx,mx)
    Y = fibanachi(215,4856,mx,my)
    px = periodx(X,mx)
    py = periody(Y,my)

    for i in xrange(my):
        W[i] = (X[i] + Y[i]) % mx
    if gcd(px, py) == 1:
        pw = px * py
    else:
        for i in xrange(my):
            for j in xrange(1, my-1):
                if W[i] == W[j] and W[i + 1] == W[j + 1]:
                    pw = j - i
                    if pw != 0:
                        z = True
                        break
            if z:
                break


def digits_number(value):
    return len(str(value))

def to_system(sys, value):
    newValue = 0
    digits = to_digits(value)
    digits_num = digits_number(value)
    return sum(map(lambda (k,v): k*v,
        izip(
            digits,
            map(lambda (k,v): k**v,
                izip(
                    repeat(sys),
                    reversed(range(digits_num)))))))

def to_digits(value):
    return map(lambda c: ord(c) - ord('0'), list(str(value)))

def to_number(array):
    return reduce(lambda a,x: a*10+x, array)

def max_digit(value):
    return max(to_digits(value))

def second_max_digit(value):
    return sorted(to_digits(value))[-1]

def take(method, count):
    return (k for _,k in izip(xrange(count), method))

def join_sequence(xiterator, yiterator, length=None, seed=2**63-1, plus=True):
    if isinstance(xiterator, list):
        xlist = xiterator
    else:
        xlist = [k for i,k in izip(xrange(length), xiterator)]
    x = xlist[int(math.fabs(seed) % len(xlist))]
    if plus:
        func = lambda x: int(math.fabs((x + yiterator.next()) % len(xlist)))
    else:
        func = lambda x: int(math.fabs((x - yiterator.next()) % len(xlist)))
    while True:
        x = xlist[func(x)]
        yield x


def main():
    first = map(lambda x: random.randint(0, 10000), range(100))
    second = knut(1283494)
    for _,k in izip(xrange(10), join_sequence(first, second)):
        print k


if __name__ == '__main__':
    main()

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


def exp(a, m):
    l = 1
    r = a
    while r % m != 1:
        r *= a
        if r > m:
            r = r % m
        l += 1
    return l


def main():
    l = levin(12348101, 12049912)
    p = period(l)
    print p.find(1000)

if __name__ == '__main__':
    main()
