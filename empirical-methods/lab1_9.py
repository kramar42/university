#! /usr/bin/env python

class Random:
    def __init__(self, seed, g):
        self.m = Martin_LusherMethod(seed * 892412);
        self.k = KnutMethod(seed % 42210)
        self.seed = seed

    def getNext(self):
        self.seed += k.getNext()
        self.seed -= kov.getNext()
        self.x = self.seed
        return self.x

def main():
    r = Random(42, 294)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

