#ifndef DRZEWO2_HPP
#define DRZEWO2_HPP

struct Wezel{
    int wartosc;
    Wezel  *lewy; //wskaźnik do następnego elementu listy
    Wezel  *prawy;
};

class Drzewo2 {
    private: // hermatyzacja danych 
        Wezel *korzen;
        Wezel *stworzWezel(int wartosc);
    
    public: //interfejs publiczny (API klasy)
        Drzewo2(); //konstruktor
        ~Drzewo2();//destruktor, posprzątanie po klasie 
        // memory leak
        void Dodaj(int);
        void Wyswietl();
        bool Usun();
        
};
#endif
