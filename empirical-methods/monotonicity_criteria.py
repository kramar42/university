#! /usr/bin/env pyton

from math import pi
from converter import to_digits

tau = 2*pi
def factorial(n):
    return sqrt(tau*n)*(n/e)**n

def doMPos(A, s_lenghts):
    i = 1
    k = 0
    i0 = -1
    while i != n - 1:
        if A[i - 1] > A[i]:
            if i == n - 2:
                s_lenghts.append(k)
                k = 1;
                s_lenghts.append(k)
                break
            k = i - i0 - 1
            i0 = i
            i = i + 2
            s_lenghts.append(k)

            if i == n - 1:
                if A[i - 1] > A[i]:
                    k = 1
                else:
                    k = 2
                s_lenghts.append(k)
                break

            if i == n:
                break
        else:
            i += 1
    return s_lenghts

def monotonicity_criteria(random):
    n = 880
    m = 8
    s_lenghts = []
    A = [k for i,k in zip(range(n), random)]
    L = to_digits(doMPos(A))
    s_number = [0] * n
    PirsonS = 0
    t = 5
    pp = [0] * n
    pr = [0] * n
    pt = [0] * n

    for i in L:
        if i == L[i]:
            s_number[i] += 1

    for i in range(len(L)):
        pp[i] = s_number[i] / len(L)
        pr[i] = 1 / factorial(L[i]) - 1 / factorial(L[i] + 1)
        if L[i] >= t:
            pr[i] = 1 / factorial(s_number[i])
        PirsonS = +((pp[i] - pr[i]) ** 2) / pr[i]

    return PirsonS * n
