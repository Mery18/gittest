#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# slowa.py
#
#
import json
from random import randint

def pobierzSlowa():
    slowa = [] #pusta lista

    ile = raw_input("Ile słów podasz?: ")
    for i in range(int (ile)):
         slowo = raw_input("Podaj słow: ")
         slowa.append(slowo.strip().lower())
    return slowa

def zapiszDane(dane):

    plik = open('slowa.txt', 'w')
    json.dump(dane, plik)
    plik.close()

def czytajDane():
    odp = raw_input('Czy załadować dane(t/n)? ').lower()
    lista = []
    if odp == 't':
        plik = open('slowa.txt','r')
        lista = json.load(plik)
        plik.close()
    return lista

def losujSlowo(slowa):
    indeks = randint(0, len(slowa) - 1)
    return slowa[indeks]

def przygotujSlowo(slowo, ilepustych):
    indeksy = [] # pusta lista na indeksy
    for i in range(ilepustych):
        indeksy.append(randint(0, len(slowo) - 1))
    print indeksy

def main(args):
    slowa = czytajDane()
    if not slowa: # pusta lista
        slowa = pobierzSlowa()
        zapiszDane(slowa)

    slowo = losujSlowo(slowa)
    ilepustych = raw_input('Ile liter odgadniesz?(max: %s)' %len(slowo))
    odgadnij = przygotujSlowo(slowo, int (ilepustych))
    return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
