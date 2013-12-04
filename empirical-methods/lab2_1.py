#! /usr/bin/env python

from math import sqrt, pi, e
from random import randint

tau = 2*pi

def criteria(sequence, t):
    r = t - 1
    f = 0

    while r > 0:
        print 'Next iteration...'
        m = sequence[0]
        s = 0
        for i in range(1, r):
            if sequence[i] > m:
                s = i
                m = sequence[s]
        f = r * f + s - 1

        print 'Swapping elements ', r, ' and ', s, '...'
        tmp = sequence[r]
        sequence[r] = sequence[s]
        sequence[s] = tmp

        r = r - 1
    return f

def setT(self, t):
    while not self.groupsIsTrue(t):
        t = t - 1
    return t

def groupsIsTrue(self, t):
    n = len(self.randomNumbers) / t
    for j in range(n):
        for i in range(t - 1):
            for k in range(i + 1, t):
                if self.randomNumbers[j * t + i] == self.randomNumbers[j * t + k]:
                    return False
    if (len(self.randomNumbers) % t) != 0:
        return False
    return True

def experimentalProbability(self, i):
    return float(self.permutationsFrequencies[i]) / self.n

def setPermutationsFrequencies(self):
    self.permutationsFrequencies = [0] * self.permutationsNumber

    for j in range(self.n):
        f = self.findNumbPermutation(j)
        self.t = self.permutationsFrequencies[f]
        self.permutationsFrequencies[f] = self.t + 1
    return self.permutationsFrequencies

def findNumbPermutation(self, j):
    t = self.t
    r = t
    f = 0

    while r > 0:
        s = self.maxNumberIndex(j, r)
        s1 = s - j * t + 1
        f = r * f + s1 - 1
        tmp = self.randomNumbers[j * self.t + r]
        self.randomNumbers[j * t + r] = self.randomNumbers[j * t + s]
        self.randomNumbers[j * t + s] = tmp

        r = r - 1

    return f

def maxNumberIndex(self, j, r):
    s = 0
    maxNumber = self.randomNumbers[j * self.t]

    for i in range(1, r):
        if self.randomNumbers[j * self.t + i] > maxNumber:
            maxNumber = self.randomNumbers[j * self.t + i]
            s = i

    return s

def factorial(n):
    return sqrt(tau*n)*(n/e)**n

def main():
    n = 2**14
    m = 2**20

    sequence = list()
    for _ in xrange(n):
        sequence.append(randint(0,m))

    print criteria(sequence, len(sequence))

if __name__ == '__main__':
    main()

