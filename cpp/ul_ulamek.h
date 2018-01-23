#ifndef ULAMEK_H
#define ULAMEK_H 
/*
 * plik naglowkowy klasy Ulamek
 * 
 * 
 */


class Ulamek {
private:
    int licznik;    
    int mianownik;
public:
    Ulamek(int, int);
    void zapisz( int, int);
    void wypisz();
     int get_l();
     int get_m();
     void skracaj(); // metoda drukuje skrocona postać ułamka 
};
#endif
