#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  witaj.py
#  
#  
ROK_TERAZ = 2017
ROK_PYTHON = 1991

def parzyste(n):
    ile = list(range(0, n+1, 2))
    print(ile)
    return len(ile)

def main(args):
    
    imie= input("Jak sie nazywasz? ")
    print ("Witaj") , imie
    
    wiek = int(input("Ile masz lat?"))
    rok_urodzenia = ROK_TERAZ
    print("Rok urodzenia: ", 2017 - wiek)
    
    if rok_urodzenia < ROK_PYTHON:
        print("Jestem mlodszy")
    elif rok_urodzenia > ROK_PYTHON:
        print("Jestem starszy")
    else:
        print("Mamy tyle samo lat!")
    
    n = int (input("Podaj liczbę: "))
    print("Parzyste: ", parzyste(n))
    
    
    return 0

if __name__ == '__main__':
    
    
    import sys
    sys.exit(main(sys.argv))
