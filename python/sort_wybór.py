#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sortowanie przez wybór

from random import randint

lista = []
n = 10

for i in range(n):
    lista.append(randint(0,100))

print lista

def sort_wybor(lista):
    for i in range(n):
        k = i
        for j in range(i, n):
            if lista[j] < lista[k]:
                k = j
        tmp = lista[i]
        lista[i] = lista[k]
        lista[k] = tmp
    return lista

print sorted(lista)
print sort_wybor(lista)
