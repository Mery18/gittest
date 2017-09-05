#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  witaj.py
#  
#  
    ROK_TERAZ = 2017
    ROK_PYTHON = 1991

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
    
    return 0

if __name__ == '__main__':
    
    
    import sys
    sys.exit(main(sys.argv))
