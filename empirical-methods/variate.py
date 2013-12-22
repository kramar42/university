#! /usr/bin/env python
# -*- encoding: utf-8 -*-

# variant: 9
# tasks: ['beta-distribution', 't-distribution']

from random import normalvariate, gammavariate

parameters = {'beta': {'alpha': 6.1, 'beta': 7.9}, 't': {'k': 3}}

def chisquaredvariate(k):
    return sum(map(lambda x:x*x,(stdnormvariate() for _ in xrange(k))))

def stdnormvariate():
    return normalvariate(0, 1)

def tvariate(k):
    return stdnormvariate() / (chisquaredvariate(k) / k) ** 0.5

def betavariate(alpha, beta):
    x1 = gammavariate(alpha, 1)
    return x1 / (x1 + gammavariate(beta, 1))

def main():
    for _ in xrange(50):
        print betavariate(**parameters['beta'])
    print
    for _ in xrange(50):
        print chisquaredvariate(**parameters['t'])

if __name__ == '__main__':
    main()
