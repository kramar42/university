#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Варіант 10
# Визначити середній час виконання та кількість кроків програми обчислення
# добутку двох векторів. Вектори та  час виконання кожного блоку програми
# визначити самостійно

from itertools import permutations
from operator import __add__

times = [5, 10, 30, 10, 20]
nodes = [(1, 2, 1),
         (2, 3, 0.9),
         (3, 4, 1),
         (4, 2, 1),
         (2, 5, 0.1)]
matrix = None

def makeMatrix(nodes, size):
    matrix = [row[:] for row in [[0] * size] * size]
    for i, j, k in nodes:
        matrix[i-1][j-1] = k
    for i in xrange(size):
        matrix[i][i] = 1 - sum(matrix[i]) + matrix[i][i]
    return matrix

class Markov:
    def __init__(self, matrix, times):
        self.matrix = matrix
        self.times = times
        self.time = 0
        self.steps = 0
        self.size = len(times)
        self.e = 0.001
        self.probability = [0] * self.size
        self.probability[0] = 1

    def run(self):
        while 1 - self._probability()[-1] > self.e:
            self.time += sum([self.probability[i] * self.times[i]
                                for i in xrange(self.size)])
        return self.probability

    def _probability(self):
        self.probability = [sum([self.probability[j] * self.matrix[j][i]
                                    for j in xrange(self.size)])
                                for i in xrange(self.size)]
        self.steps += 1
        return self.probability


def main():
    matrix = makeMatrix(nodes, len(times))
    graph = Markov(matrix, times)

    print 'Probability vector', graph.run()
    print 'Number of steps:', graph.steps
    print 'Elapsed time:', graph.time


if __name__ == '__main__':
    main()

