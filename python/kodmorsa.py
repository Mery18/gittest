#!/usr/bin/env python
# -*- coding: utf-8 -*-


def koduj(napis):
<<<<<<< HEAD
    litery = {'a': '*-', 'b': '-***', 'c': '-*–*','d': '–**', 'e': '*', 'f': '**–*', 'g': '–**','h': '****', 'i': '**', 'j': '*–––', 'k': '–*–', 'l': '*–**', 'm': '––', 'n': '–*', 'o': '–––', 'p': '*––*', 'r': '*–*', 's': '***', 't':'–', 'u': '**–', 'w': '*––', 'v': '***–', 'x': '–**–', 'y': '–*–', 'z': '––**'}
=======
    litery = {'a': '*-', 'b': '-***', 'c': '-*–*,'d': '–**', 'e': '*', 'f': '**–*', 'g': '–**','h': '****', 'i': '**', 'j': '*–––', 'k': '–*–', 'l': '*–**', 'm': '––', 'n': '–*', 'o': '–––', 'p': '*––*', 'r': '*–*', 's': '***', 't':'–', 'u': '**–', 'w': '*––', 'v': '***–', 'x': '–**–', 'y': '–*–', 'z': '––**'}
>>>>>>> ea0a0a4bd8465109d531722a6b140f34aedbd7bf
    for litera in napis:
        if litera != ' ':
            print litery[litera.lower()]

def main(args):
    napis = raw_input("Podaj napis")
    koduj("napis")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
