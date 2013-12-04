#! /usr/bin/env python

class Martin_LusherMethod:
    def __init__(self, marsalia, marsalia_N, lusher_N):
        self.marsalia_N = marsalia_N
        self.lusher_N = lusher_N
        self.marsalia = marsalia
        self.counter = 0

    def generateMarsaliaNumbers(self):
        numbers = []
        for i in xrange(self.marsalia_N):
            numbers.append(marsalia.getNext())
        self.counter = self.lusher_N

    def getNext(self):
        if self.counter == 0
            self.generateMarsaliaNumbers()
        nextNumber = self.numbers[0]
        del self.numbers[0]
        self.counter -= 1
        return nextNumber

def main():
    r = Martin_LusherMethod(marsalia, 17, 10)
    for i in range(10):
        print r.getNext()

if __name__ == '__main__':
    main()

