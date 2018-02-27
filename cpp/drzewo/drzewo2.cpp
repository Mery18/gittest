#include <iostream>
#include "drzewo2.hpp"

Drzewo2::Drzewo2(){
    korzen = NULL;
}
Drzewo2::~Drzewo2(){
   while(Usun()){;};
}
void Drzewo2::Dodaj(int wartosc){
        ELEMENT *el = new ELEMENT;
        el ->wartosc = wartosc;
        el ->nast =NULL;
        if (korzen == NULL){
            korzen = el;
            tail = el;
        } else {    
            tail ->nast = el; //ustawinie wskanika nast dotychczasowego 
            // osatniego elementu adresu nowego ostatniego elementu 
            tail = el; // aktualizujemy wskaźnik ogn, aby wskazywał na nowy dodany element 
        
        }
}
void Drzewo2::Wyswietl(){
    ELEMENT *el = korzen;
    while (el != NULL) {
        std::cout << el->wartosc << " ";
        el = el -> nast;
        }
        std::cout << std::endl;
}

bool Lista::Usun(){
    if (korzen != NULL){
        if(head == tail){ // usunięcie ostatniego elementu
            delete korzen ;
            korzen  = NULL;
            tail = NULL;
        }else {
            ELEMENT *el = head;
            while(el ->nast != tail){ // szukam przedostniego elementu 
                el = el ->nast;
                }
                delete el ->nast;
                el ->nast = NULL;
                tail = el;
            }
            return true;
}
    return false;
}
