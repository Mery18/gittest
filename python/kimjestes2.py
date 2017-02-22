#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#


#~def main(args):
    #~return 0

#~if __name__ == '__main__':
    #~import sys
    #~sys.exit(main(sys.argv))
teraz = 2016 # biężacy rok
rok_pythona = 1991 # rok powstania Pythona

imie = raw_input("Imię ")
if len(imie.strip()) == 0 or not imie.isalpha():
    imie = "Nieznajomy"
elif imie[0].islower():
    imie = imie[0].upper() + imie[1: ] # imię z dużej litery

wiek = raw_input("Ile lat? ")
if wiek.isdigit() and int(wiek) >= 18 and int(wiek) < 80:
    rok_urodzenia = teraz - int (wiek)
else:
    print "Błędny wiek"
    wiek = 0
    rok_urodzenia = teraz


wiek_pythona = teraz - rok_pythona

print "Cześć", imie, "Jestem Python"
print "Urodziłeś się w %s roku." % rok_urodzenia
print "Powstałem w %s roku i mam %s lat." % (rok_urodzenia, wiek_pythona)

if wiek_pythona > int(wiek):
    print "Jestem starszy! "
elif wiek_pythona == int(wiek):
    print "Mamy tyle samo lat!"
else:
    print "Jestesm młodszy!"

