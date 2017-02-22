#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#

#
#
def sil_rekn(n):
    if n ==0:
        return 1
    return sil_rek(n-1)*n

def sil_it(n):
    wynik = 1
    for i in range (1, n +1):
            wynik = wynik *i
    return wynik

def main(args):
    x = int(raw_input("Podaj liczbe: "))
    print "sil_it(%s) = %s" % (x, sil_it(liczba))
    print "sil_rek(%s) = %s" % (x, sil_rek(liczba))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

