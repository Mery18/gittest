#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sqlite3

import os
from peewee import *
from dane import *

baza_plik = "pracownicy.sqlite3"
baza = SqliteDatebase(baza-plik)


def wyniki(cur):
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_1(cur):
    cur.execute("""
        SELECT nazwisko, imie, tbKlasy.Klasa
        FROM tbuczniowie, tbKlasy
        WHERE tbuczniowie.KlasaID = tbKlasy.IDKlasy
        AND Klasa LIKE '1A'
    """) #pojedyncze polecenie
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_2(cur):
    cur.execute("""
        SELECT  MAX(EgzHum)
        FROM tbUczniowie
    """) #pojedyncze polecenie
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_3(cur):
    cur.execute("""
        SELECT   AVG(EgzMat), tbKlasy.Klasa
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
        AND Klasa LIKE '1A'

    """) #pojedyncze polecenie
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_4(cur):
    cur.execute("""
        SELECT   Imie, Nazwisko, tbOceny.Ocena, tbPrzedmioty.Przedmiot
        FROM tbUczniowie, tbOceny, tbPrzedmioty
        WHERE tbOceny.UczenID = tbUczniowie.IDUcznia
        AND tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND Nazwisko LIKE 'Nowak'
    """) #pojedyncze polecenie
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_5(cur):
    cur.execute("""
        SELECT   Datad, AVG(Ocena), Przedmiot
        FROM tbOceny, tbPrzedmioty
        WHERE tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND strftime('%m', datad) LIKE 10
        AND Przedmiot LIKE 'fizyka'


    """) #pojedyncze polecenie
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_c(cur):
    cur.execute("""
        SELECT siedziba, SUM(placa) AS pensje
        FROM pracownicy, dzial
        WHERE  pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensje ASC
    """) #pojedyncze polecenie
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_e(cur):
    cur.execute("""
        SELECT nazwisko, stanowisko,
        pracownicy.placa *
        (SELECT premia.premia
        FROM premia
        WHERE pracownicy.stanowisko = premia.id)
        AS premia
        FROM pracownicy
        ORDER BY premia DESC
    """)
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_f(cur):
    cur.execute("""
        SELECT AVG(placa)
        FROM pracownicy
        WHERE imie LIKE ('%a')
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

    cur.execute("""
        SELECT AVG(placa)
        FROM pracownicy
        WHERE imie NOT LIKE ('%a')
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_g(cur):
    cur.execute("""
        SELECT imie, nazwisko, stanowisko,
        (JulianDay())
        FROM
        WHERE
    """)

    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_d(cur):
    nazwa1 = input("Podaj nazwę działu: ")
    nazwa2= input("Podaj nazwę siedziby: ")
    print(nazwa1)
    print(nazwa2)

    cur.execute("""
        SELECT nazwisko, imie, dzial.id, dzial.nazwa, dzial.siedziba
        FROM pracownicy, dzial
        WHERE pracownicy.id dzial = dzial.id AND dzial.nazwa = ?
        AND dzial.nazwa = ?
        AND siedziba = ?
    """, (nazwa1, nazwa2s))
    wyniki = cur.fetchall() # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def dodaj():
    cur.execute("""
        INSERT INTO tbKlasy
        VALUES (?,?,?,?)
    """, [None, '3C', 2015, 2017])

def aktualizuj(cur):
    cur.execute("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE idklasy = ?
    """, [ '3D', 13])

def usun(cur):
    cur.execute('DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru = ?', ['3B', 2015])


def aktualizuj_2(cur):
    cur.execute("""
        UPDATE tbUczniowie
        SET EgzJez = ?
        WHERE IDklasy = ?
    """, [ 'Paulina Dziedzic', 35])


def main(args):
    con = sqlite3. connect('szkola.db')
    cur = con.cursor() #utworzenie kursora
    con.row_factory = sqlite3.Row

    #dodaj(cur)
    #aktualizuj(cur)
    #usun(cur)
    aktualizuj_2(cur)
    con.commit()
    wyniki(cur.execute('SELECT * FROM tbKlasy'))

    #kw_d(cur)
   # kw_c(cur)
    #kw_e(cur)
    #kw_f(cur)
    #kw_1(cur)
    #kw_2(cur)
    #kw_3(cur)
    #kw_4(cur)
    #kw_5(cur)


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
