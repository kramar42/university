#! /usr/bin/evn python

from itertools import repeat, izip

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
