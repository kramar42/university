#! /usr/bin/env python

from itertools import izip
import math


task = {
        'variant': 11,
        'tasks_variants': [2, 1, 0],
        'tasks': ['!eichenauer', '!knut', '!kovey', 'levin', '!lehmer',
                  'martin_lusher', 'mclaren_marsalia', 'polinomial']
       }


class digits:
    '''Stores integer as list of digits'''
    def __init__(self, value):
        self.digits = map(lambda c: ord(c) - ord('0'), list(str(value)))

    def __getitem__(self, i):
        return self.digits[i]

    def value(self):
        return reduce(lambda a,x: a*10+x, self.digits, 0)

    def next(self):
        return self.digits.pop()


def euclid(a, b):
    '''Returns GCD of a and b'''
    if b == 0: return (1, 0, a)
    x1, x2, y1, y2 = (0, 1, 1, 0)

    while b > 0:
        q = a / b
        r = a - q * b
        x, y = (x2 - q * x1, y2 - q * y1)
        x1, x2 = x, x1
        a, b = b, r
    return (x2, y2, a)


def inversed(a, m):
    '''Returns x, such that a * x mod m = 1'''
    x, y, d = euclid(a, m)
    if d == 1:
        return x
    return 0

def middle(*args):
    s = ''.join(map(str, args))
    diff = len(s) / 2
    shift = diff / 2

    s = s[shift: -(diff - shift)]
    return s



class knut:
    def __init__(self, seed):
        self.x = seed
        self.seed = seed

    def __iter__(self):
        return self

    def case0(self):
        if self.x < 5000000000L:
            self.x += 5000000000L
        self.case1()
    def case1(self):
        self.x = int(math.floor((self.x * self.x) / 100000L)) % 10000000000L
        self.case2()
    def case2(self):
        self.x = 1001001001L * self.x % 10000000000L
        self.case3()
    def case3(self):
        if self.x < 100000000L:
            self.x += 9814055677L
        else:
            self.x = 10000000000L - self.x
        self.case4()
    def case4(self):
        first5 = self.x % 100000L
        self.x = first5 * 100000L + (self.x / 100000L)
        self.case5()
    def case5(self):
        self.x = 1001001001L * self.x % 10000000000L
        self.case6()
    def case6(self):
        d = digits(self.x)
        for i in xrange(len(d.digits)):
            if d.digits[i] != 0:
                d.digits[i] -= 1
        self.x = d.value()
        self.case7()
    def case7(self):
        if self.x < 100000L:
            self.x = self.x * self.x + 99999L
        else:
            self.x -= 99999L
            self.case8()
    def case8(self):
        while self.x < 1000000000L:
            self.x *= 10
        self.case9()
    def case9(self):
        self.x = int(math.floor((self.x * (self.x - 1) / 100000L))) % 10000000000L

    def next(self):
        for i in xrange(digits(self.x)[0]):
            getattr(self, 'case' + str(digits(self.x)[1]))()
        return self.x


class kovey:
    def __init__(self, seed, l=64):
        self.x = seed
        self.seed = seed
        self.l = 2 << l

    def __iter__(self):
        return self

    def next(self):
        self.x = self.x * (self.x + 1) % self.l
        return self.x


class eichenauer:
    def __init__(self, a, c, m, seed):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def __iter__(self):
        return self

    def next(self):
        if self.x == 0:
            self.x = sys.maxint
        else:
            self.x = (self.a * inversed(self.x, self.m) + self.c) % self.m
        return self.x

class von_neumann():
    def __init__(self, x):
        self.x = x
        self.size = len(str(x))

    def __iter__(self):
        return self

    def next(self):
        self.x = int(middle(self.x ** 2))
        return self.x

class mochli:
    def __init__(self, x, k):
        self.a = [x] + [i for i,_ in izip(von_neumann(x), xrange(k-1))]
        self.k = k

    def __iter__(self):
        return self

    def next(self):
        x = self.a[0]
        # middle of concat first & last elements in list
        self.a.append(int(middle(self.a[0], self.a[-1])))
        del self.a[0]

        return x

class lehmer:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def __iter__(self):
        return self

    def next(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def potential(self, bound=100):
        potential = 0
        accum = (self.a - 1)
        for i in xrange(bound):
            if accum % self.m == 0:
                return potential
            accum *= (self.a - 1)
            potential += 1
        # potential if out of bounds
        return None

class marsalia:
    def __init__(self, seed):
        self.m = 2 ** 32
        self.seed = seed
        self.buf = [seed + i for i in xrange(55)]

    def __iter__(self):
        return self

    def next(self):
        x = (self.buf[55 - 24] * self.buf[55 - 55]) % self.m
        del self.buf[0]
        self.buf.append(x)
        return x

class quadratic_congruence:
    def __init__(self, d, a, c, m, seed):
        self.d = d
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def __iter__(self):
        return self

    def next(self):
        self.x = (self.d * self.x ** 2 + self.a * self.x + self.c) % self.m
        return self.x


def main():
    #dh = darham(le, 10)
    #le = levin(12348101, 1249912)
    #ml = martin_lusher(ma, 500, 55)
    #mm = mclaren_marsalia(le, ma, 100)
    #pl = polinomial(2134512908)
    #ra = random(23481920, 294)
    ei = eichenauer(104711, 104723, 104717, 104729)
    fn = von_neumann(47382384910295619L)
    kn = knut(3848239084290384901283494L)
    kv = kovey(3284910283328490128448L)
    lm = lehmer(41+1, 43, 41**10, 42**10)
    ma = marsalia(128390238901238141L)
    mo = mochli(43894218902L, 5)
    qc = quadratic_congruence(348348820L, 3849023L, 38490234L, 2**64, 42)

    for _,k in izip(xrange(10), qc):
        print k


if __name__ == '__main__':
    main()

