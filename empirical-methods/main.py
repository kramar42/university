#! /usr/bin/env python

from darham_method import darham
from eichenauer_method import eichenauer
from knut_method import knut
from kovey_method import kovey
from levin_method import levin
from lincong_method import lincong
from marsalia_method import marsalia
from martin_lusher_method import martin_lusher
from mochli_method import mochli
from mclaren_marsalia_method import mclaren_marsalia
from polinomial_method import polinomial
from quadcong_method import quadcong
from random_method import random
from converter import take
from find_period import period

def main():
    le = levin(12348101, 1249912)
    dh = darham(le, 10)
    ei = eichenauer(25454549, 24, 5757, 9090)
    kt = knut(1283494).iterator()
    kv = kovey(32849102834)
    lc = lincong(2**63-1, 2**62+1, 2**61+1, 1238417890234)
    ma = marsalia(12839041)
    ml = martin_lusher(ma, 500, 55)
    mo = mochli(418902, 21490, 231480, 1249912).generator()
    mm = mclaren_marsalia(le, ma, 100)
    pl = polinomial(2134512908)
    qc = quadcong(2**62+1, 2**63-1, 2**62+1, 2**61+1, 1238417890234)
    ra = random(23481920, 294)

    print period(le).find(1000)


if __name__ == '__main__':
    main()
