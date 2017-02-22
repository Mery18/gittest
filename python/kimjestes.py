#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#


#~def main(args):
    #~return 0

#~if __name__ == '__main__':
    #~import sys
    #~sys.exit(main(sys.argv))

imie = raw_input("Imię ")
print "Cześć", imie, "Jestem Python"

wiek = raw_input("Ile lat? ")
teraz = 2016
rok_urodzenia = teraz - int (wiek)
print "Urodziłeś się w %s roku." % rok_urodzenia


rok_pythona = 1991
wiek_pythona = teraz - rok_pythona
print "Powstałem w %s roku i mam %s lat." % (rok_urodzenia, wiek_pythona)

if wiek_pythona > int(wiek):
    print "Jestem starsza! "
else:
    print "Jestesm młodsza!"
