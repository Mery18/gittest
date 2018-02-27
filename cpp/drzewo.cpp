#include <iostream>
#include "drzewo.hpp"

Wezel::Wezel(){
    head = NULL;
    tail = NULL;
}
Wezel::~Wezel(){
   while(Usun()){;};
}
void Wezel::Dodaj(int wartosc){
        if (korzen == NULL) { // drzewo jest puste!
        korzen = stworzWezel(wartosc); // utworzenie 1. elementu
    } else {
        if (wartosc < wezel->wartosc) { // wstawiamy wartość mniejszą // wstawiamy wartość do lewego poddrzewa 
            if(wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc);  // rekurencyjne wywołanie dodawanie do lewego poddrzewa
            } else {  // lewy potomek nie istnieje
                wezel->lewy = stworzWezel(wartosc);  // tworzymy nowy wezel
            }
        } else { // wstawiamy wartość większą // wstawiamy wartość do lewgo poddrzewa 
            if(wezel->prawy != NULL) {
                dodajWezel(wezel->prawy, wartosc);  // rekurencyjne wywołanie dodawanie do lewego poddrzewa
            } else {  // prawy potomek nie istnieje
                wezel->prawy = stworzWezel(wartosc);  // tworzymy nowy wezel
            }
        }
    }
}
void Lista::Wyswietl(){
     if (wezel != NULL) { // jeżeli węzeł nie jest pusty
        //rekurencyjnie wyswietl lewe poddrzewo
        wyswietlRosnoco(wezel ->lewy);
        // wypisz wartosc aktualnego węzła
        cout << wezel -> wartosc << ",";
        // rekurencyjnie wyswietl prawe poddrzewo
        wyswietlRosnoco(wezel ->prawy);
}

bool Lista::Usun(){
     cout << "posortowane drzewo (niemalejąco): ";
        wyswietlRosnoco(korzen);
        
        delete korzen; //zwonienie wykporzystanej pamięci 
}
    return false;
}

















