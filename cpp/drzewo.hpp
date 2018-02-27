#ifndef DRZEWO_HPP
#define DRZEWO_HPP

struct Wezel{
    int wartosc;
    Drzewo *lewy;
    Drzewo *prawy;
    
};

class Drzewo {
    private: // hermatyzacja danych 
        Drzewo *head;
        Drzewo *tail;
    
    public: //interfejs publiczny (API klasy)
        Wezel(); //konstruktor
        ~Wezel();//destruktor,
        // memory leak
        void dodajWezel(int);
        void wyswietlRosnoco();
        bool Usun();
        
};
#endif


