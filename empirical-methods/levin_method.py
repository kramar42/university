#! /usr/bin/env python

import sys
import random
import math

class levin:
    def __init__(self, seed, modulus):
        self.seed = seed
        self.currentX = seed
        self.modulus = modulus
        self.t = self.GenerateConstant()

    def __iter__(self):
        return self

    def getSeed(self):
        return self.seed

    def next(self):
        self.currentX = self.currentX ** 2 % self.modulus
        return self.currentX * ScalarMutiplexBinary(self.currentX, self.t) % 2

    def GenerateConstant(self):
        randomSeed = random.randint(0, sys.maxint)
        operand = (1 << int(math.log(self.modulus) / math.log(2) + 1)) - 1
        return randomSeed & operand

def ScalarMutiplexBinary(operand1, operand2):
    logicalAnd = operand1 & operand2
    scalarMultiplex = 0
    while logicalAnd != 0:
        scalarMultiplex += logicalAnd & 1
        logicalAnd = logicalAnd >> 1
    return scalarMultiplex

def main():
    l = levin(12348101, 1249912)
    for i, k in zip(range(10), l):
        print k

if __name__ == '__main__':
    main()

