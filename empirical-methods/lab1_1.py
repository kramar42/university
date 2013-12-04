#! /usr/bin/env python

import sys
import random
import math

class LevinMethod:
    def __init__(self, seed, modulus):
        self.seed = seed
        self.currentX = seed
        self.modulus = modulus
        self.t = self.GenerateConstant()

    def getSeed(self):
        return self.seed

    def getNext(self):
        print 'New currentX:', self.currentX
        self.currentX = self.currentX ** 2 % self.modulus
        return self.currentX * ScalarMutiplexBinary(self.currentX, self.t) % 2

    def GenerateConstant(self):
        randomSeed = random.randint(0, sys.maxint)
        operand = (1 << int(math.log(self.modulus) / math.log(2) + 1)) - 1
        return randomSeed & operand

def ScalarMutiplexBinary(operand1, operand2):
    print operand1, operand2
    logicalAnd = operand1 & operand2
    scalarMultiplex = 0
    while logicalAnd != 0:
        scalarMultiplex += logicalAnd & 1
        logicalAnd = logicalAnd >> 1
    return scalarMultiplex

def main():
    r = LevinMethod(42, 17)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

